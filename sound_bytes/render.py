"""Render a parsed Score to per-instrument WAV stems plus a mixed-down WAV."""
from __future__ import annotations

import wave
from pathlib import Path
from typing import Dict, List, Sequence

import numpy as np

from .parser import Score
from .synth import render_channel


def render_score(score: Score, sr: int = 44100) -> Dict[str, np.ndarray]:
    """Return {channel_name: samples}, all padded to the same length so they line up."""
    stems = {
        name: render_channel(score.instruments[name], notes, score.tempo, sr, seed=i)
        for i, (name, notes) in enumerate(score.channels.items())
    }
    length = max((len(s) for s in stems.values()), default=0)
    return {name: np.pad(s, (0, length - len(s))) for name, s in stems.items()}


def mix(stems: Dict[str, np.ndarray]) -> np.ndarray:
    if not stems:
        return np.zeros(0)
    total = np.sum(list(stems.values()), axis=0)
    peak = float(np.max(np.abs(total))) if total.size else 0.0
    return total / peak * 0.95 if peak > 0.95 else total


def write_wav(path: Path, samples: np.ndarray, sr: int, bit_depth: int = 16) -> None:
    clipped = np.clip(samples, -1.0, 1.0)
    if bit_depth == 8:
        data = ((clipped * 127) + 128).astype(np.uint8)  # 8-bit WAV is unsigned
        width = 1
    elif bit_depth == 16:
        data = (clipped * 32767).astype("<i2")
        width = 2
    else:
        raise ValueError("bit_depth must be 8 or 16")
    with wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(width)
        f.setframerate(sr)
        f.writeframes(data.tobytes())


def write_mp3(path: Path, samples: np.ndarray, sr: int, bitrate: int = 192) -> None:
    """Encode mono samples to MP3 using the bundled LAME encoder (pip install lameenc)."""
    try:
        import lameenc
    except ImportError:
        raise RuntimeError("MP3 export needs the lameenc package: pip install lameenc")
    enc = lameenc.Encoder()
    enc.set_bit_rate(bitrate)
    enc.set_in_sample_rate(sr)
    enc.set_channels(1)
    enc.set_quality(2)  # 2 = high quality
    pcm = (np.clip(samples, -1.0, 1.0) * 32767).astype("<i2")
    path.write_bytes(bytes(enc.encode(pcm.tobytes())) + bytes(enc.flush()))


def render_to_dir(score: Score, out_dir: Path, sr: int = 44100, bit_depth: int = 16,
                  formats: Sequence[str] = ("wav",), mp3_bitrate: int = 192) -> Dict[str, List[Path]]:
    """Write every stem plus `mix` in each requested format. Returns {name: [files written]}."""
    if not formats or any(f not in ("wav", "mp3") for f in formats):
        raise ValueError("formats must be a non-empty subset of ('wav', 'mp3')")
    out_dir.mkdir(parents=True, exist_ok=True)
    stems = render_score(score, sr)
    stems_with_mix = {**stems, "mix": mix(stems)}
    paths: Dict[str, List[Path]] = {}
    for name, samples in stems_with_mix.items():
        paths[name] = []
        for fmt in formats:
            p = out_dir / f"{name}.{fmt}"
            if fmt == "wav":
                write_wav(p, samples, sr, bit_depth)
            else:
                write_mp3(p, samples, sr, mp3_bitrate)
            paths[name].append(p)
    write_player(score, {n: fs[0] for n, fs in paths.items()}, out_dir / "index.html")
    return paths


def write_player(score: Score, paths: Dict[str, Path], html_path: Path) -> None:
    """Write a tiny local HTML page with an audio player for the mix and each stem."""
    from html import escape

    rows = "\n".join(
        f"<h3>{escape(name)}</h3><audio controls loop preload=auto src=\"{escape(p.name)}\"></audio>"
        for name, p in sorted(paths.items(), key=lambda kv: kv[0] != "mix")
    )
    html_path.write_text(
        "<!doctype html><meta charset=utf-8>"
        f"<title>{escape(score.title)}</title>"
        "<style>body{font:16px monospace;background:#111;color:#8f8;max-width:560px;margin:2em auto}"
        "audio{width:100%}</style>"
        f"<h1>{escape(score.title)}</h1><p>{score.tempo:g} bpm</p>\n{rows}\n"
    )

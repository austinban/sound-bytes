"""Render a parsed Score to per-instrument WAV stems plus a mixed-down WAV."""
from __future__ import annotations

import wave
from pathlib import Path
from typing import Dict

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


def render_to_dir(score: Score, out_dir: Path, sr: int = 44100, bit_depth: int = 16) -> Dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stems = render_score(score, sr)
    paths = {}
    for name, samples in stems.items():
        paths[name] = out_dir / f"{name}.wav"
        write_wav(paths[name], samples, sr, bit_depth)
    paths["mix"] = out_dir / "mix.wav"
    write_wav(paths["mix"], mix(stems), sr, bit_depth)
    write_player(score, paths, out_dir / "index.html")
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

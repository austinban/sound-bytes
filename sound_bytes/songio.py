"""Convert between a parsed Score and the editor's JSON model (notes with start/length), and write .sb text."""
from __future__ import annotations

import math
import re
from typing import Any, Dict, List

from .parser import DRUMS, WAVE_TYPES, Score

_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")
_PARAM_KEYS = ("duty", "volume", "attack", "decay", "sustain", "release", "sub", "detune", "echo",
               "vibrato", "vibrato_rate", "vibrato_delay", "slide", "slide_time",
               "pwm", "pwm_rate", "tremolo", "tremolo_rate", "ratio", "index", "index_decay", "bits", "hold")


def midi_to_name(midi: int) -> str:
    return f"{_NAMES[midi % 12]}{midi // 12 - 1}"


def score_to_json(score: Score) -> Dict[str, Any]:
    tracks: List[Dict[str, Any]] = []
    end = 0.0
    for name, inst in score.instruments.items():
        pos, notes = 0.0, []
        for n in score.channels.get(name, []):
            if n.kind == "pitch":
                notes.append({"start": pos, "len": n.beats, "midi": n.midi})
            elif n.kind == "drum":
                notes.append({"start": pos, "len": n.beats, "drum": n.drum})
            pos += n.beats
        end = max(end, pos)
        tracks.append({"name": name, "wave": inst.wave, "params": dict(inst.params), "notes": notes})
    bars = score.bars or max(math.ceil(end / 4), 4)
    return {"title": score.title, "tempo": score.tempo, "bars": max(bars, math.ceil(end / 4)), "tracks": tracks}


def _g(x: float) -> str:
    return f"{x:g}"


def json_to_text(song: Dict[str, Any]) -> str:
    """Validate the editor's JSON and write a .sb score. Raises ValueError on bad input."""
    try:
        tempo = float(song["tempo"])
        bars = int(song["bars"])
        tracks = song["tracks"]
        title = str(song.get("title", "untitled")).replace("\n", " ").strip() or "untitled"
    except (KeyError, TypeError, ValueError):
        raise ValueError("song needs title, tempo, bars and tracks")
    if tempo <= 0 or not 1 <= bars <= 512:
        raise ValueError("tempo must be positive and bars between 1 and 512")

    lines = [f"title: {title}", f"tempo: {_g(tempo)}", f"bars: {bars}", ""]
    seen = set()
    channel_lines: List[str] = []
    total_beats = bars * 4.0

    for t in tracks:
        name, wave = t.get("name"), t.get("wave")
        if not isinstance(name, str) or not _NAME_RE.match(name) or name in seen:
            raise ValueError(f"bad or duplicate track name {name!r}")
        if wave not in WAVE_TYPES:
            raise ValueError(f"bad wave {wave!r} on track {name!r}")
        seen.add(name)
        params = t.get("params", {})
        extras = " ".join(f"{k}={_g(float(params[k]))}" for k in _PARAM_KEYS if k in params)
        lines.append(f"instrument {name}: {wave} {extras}".rstrip())

        notes = sorted(t.get("notes", []), key=lambda n: n["start"])
        tokens: List[str] = []
        pos = 0.0
        row: List[str] = []

        def flush() -> None:
            nonlocal row
            if row:
                channel_lines.append(f"{name}: " + " ".join(row))
                row = []

        def emit(token: str, length: float) -> None:
            nonlocal pos
            row.append(f"{token}:{_g(length)}")
            pos += length
            if abs(pos / 4 - round(pos / 4)) < 1e-9:
                flush()

        for n in notes:
            start, length = float(n["start"]), float(n["len"])
            if length <= 0 or start < 0:
                raise ValueError(f"bad note timing on track {name!r}")
            if start < pos - 1e-9:
                raise ValueError(f"overlapping notes on track {name!r} (channels are monophonic)")
            if start + length > total_beats + 1e-9:
                raise ValueError(f"note past end of song on track {name!r}")
            if start > pos:
                emit("R", start - pos)
            if wave == "noise" and n.get("drum") is not None:
                if n["drum"] not in DRUMS:
                    raise ValueError(f"noise track {name!r} needs drum K, S or H")
                emit(n["drum"], length)
            else:
                midi = n.get("midi")
                if not isinstance(midi, int) or not 12 <= midi <= 119:
                    raise ValueError(f"bad pitch on track {name!r}")
                emit(midi_to_name(midi), length)
        if pos < total_beats:
            emit("R", total_beats - pos)
        flush()
        channel_lines.append("")

    return "\n".join(lines + [""] + channel_lines).rstrip() + "\n"

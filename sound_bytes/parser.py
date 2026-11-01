"""Parser for the .sb score format.

Example:

    title: Demo
    tempo: 140
    instrument lead: pulse duty=0.25 volume=0.6
    instrument bass: triangle
    instrument drums: noise

    lead:  C5:1 E5:1 G5:2
    bass:  [C3:0.5 C3:0.5]x4
    drums: K:1 H:1 S:1 H:1

Rules:
  * `instrument NAME: @preset [key=value ...]` loads instruments/preset.json, with optional overrides.
  * `bars: N` (optional) sets the length shown in the editor.
  * Blank lines are ignored; comments start with `#` at the beginning of a line
    or after whitespace (so `C#4` is fine).
  * A note is NAME:BEATS, e.g. `C#4:0.5`. `R:1` is a rest. Default length is 1 beat.
  * Noise channels use drum names instead of pitches: K (kick), S (snare), H (hat).
  * `[ ... ]xN` repeats the bracketed tokens N times (no nesting).
  * A channel can appear on several lines; the lines are joined in order.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

DEFAULT_INSTRUMENT_DIR = Path(__file__).resolve().parent.parent / "instruments"
_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")

WAVE_TYPES = ("pulse", "triangle", "noise")
DRUMS = ("K", "S", "H")

_PITCH_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d)$")
_REPEAT_RE = re.compile(r"\[([^\[\]]*)\]\s*x(\d+)")
_SEMITONES = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


class ScoreError(ValueError):
    """Raised for any problem in a score file; message includes the line number."""


@dataclass
class Instrument:
    name: str
    wave: str
    params: Dict[str, float] = field(default_factory=dict)


@dataclass
class Note:
    kind: str  # "pitch", "rest" or "drum"
    beats: float
    midi: Optional[int] = None  # for kind == "pitch"
    drum: Optional[str] = None  # for kind == "drum"


@dataclass
class Score:
    title: str = "untitled"
    tempo: float = 120.0
    bars: Optional[int] = None
    instruments: Dict[str, Instrument] = field(default_factory=dict)
    channels: Dict[str, List[Note]] = field(default_factory=dict)


def pitch_to_midi(name: str) -> int:
    m = _PITCH_RE.match(name)
    if not m:
        raise ValueError(f"bad pitch {name!r}")
    letter, accidental, octave = m.group(1).upper(), m.group(2), int(m.group(3))
    semitone = _SEMITONES[letter] + (1 if accidental == "#" else -1 if accidental == "b" else 0)
    return 12 * (octave + 1) + semitone


def load_preset(name: str, instrument_dir: Path, lineno: int = 0) -> Tuple[str, Dict[str, float]]:
    """Load instruments/<name>.json -> (wave, params)."""
    if not _NAME_RE.match(name):
        raise ScoreError(f"line {lineno}: bad instrument preset name {name!r}")
    path = Path(instrument_dir) / f"{name}.json"
    try:
        data = json.loads(path.read_text())
        return data["wave"], {k: float(v) for k, v in data.get("params", {}).items()}
    except (OSError, ValueError, KeyError):
        raise ScoreError(f"line {lineno}: can't load instrument preset {name!r} from {path}")


def _parse_token(token: str, inst: Instrument, lineno: int) -> Note:
    name, sep, length = token.rpartition(":")
    if not sep:
        name, length = token, "1"
    try:
        beats = float(length)
    except ValueError:
        raise ScoreError(f"line {lineno}: bad duration in {token!r}")
    if beats <= 0:
        raise ScoreError(f"line {lineno}: duration must be positive in {token!r}")

    if name.upper() == "R":
        return Note("rest", beats)
    if inst.wave == "noise":
        if name.upper() not in DRUMS:
            raise ScoreError(f"line {lineno}: noise channel {inst.name!r} expects K, S, H or R, got {token!r}")
        return Note("drum", beats, drum=name.upper())
    try:
        return Note("pitch", beats, midi=pitch_to_midi(name))
    except ValueError:
        raise ScoreError(f"line {lineno}: bad note {token!r}")


def _strip_comment(line: str) -> str:
    if line.lstrip().startswith("#"):
        return ""
    return re.sub(r"\s#.*$", "", line).strip()


def parse_score(text: str, instrument_dir: Optional[Path] = None) -> Score:
    instrument_dir = Path(instrument_dir) if instrument_dir else DEFAULT_INSTRUMENT_DIR
    score = Score()
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = _strip_comment(raw)
        if not line:
            continue

        if line.startswith("instrument "):
            head, sep, rest = line[len("instrument "):].partition(":")
            name, parts = head.strip(), rest.split()
            if not sep or not name or not parts:
                raise ScoreError(f"line {lineno}: expected `instrument NAME: TYPE [key=value ...]`")
            params: Dict[str, float] = {}
            if parts[0].startswith("@"):
                wave, params = load_preset(parts[0][1:], instrument_dir, lineno)
            elif parts[0] in WAVE_TYPES:
                wave = parts[0]
            else:
                raise ScoreError(f"line {lineno}: unknown wave {parts[0]!r} (choose from {', '.join(WAVE_TYPES)})")
            for kv in parts[1:]:
                key, eq, val = kv.partition("=")
                try:
                    params[key] = float(val)
                except ValueError:
                    raise ScoreError(f"line {lineno}: bad parameter {kv!r}")
            score.instruments[name] = Instrument(name, wave, params)
            continue

        key, sep, rest = line.partition(":")
        key = key.strip()
        if not sep:
            raise ScoreError(f"line {lineno}: can't understand {line!r}")
        if key.lower() == "title":
            score.title = rest.strip()
        elif key.lower() == "bars":
            try:
                score.bars = int(rest)
            except ValueError:
                raise ScoreError(f"line {lineno}: bad bars {rest.strip()!r}")
        elif key.lower() == "tempo":
            try:
                score.tempo = float(rest)
            except ValueError:
                raise ScoreError(f"line {lineno}: bad tempo {rest.strip()!r}")
            if score.tempo <= 0:
                raise ScoreError(f"line {lineno}: tempo must be positive")
        else:
            inst = score.instruments.get(key)
            if inst is None:
                raise ScoreError(f"line {lineno}: channel {key!r} has no `instrument` declaration above it")
            expanded = _REPEAT_RE.sub(lambda m: (" " + m.group(1) + " ") * int(m.group(2)), rest)
            if "[" in expanded or "]" in expanded:
                raise ScoreError(f"line {lineno}: unmatched or nested bracket in repeat")
            notes = score.channels.setdefault(key, [])
            notes.extend(_parse_token(tok, inst, lineno) for tok in expanded.split())
    return score

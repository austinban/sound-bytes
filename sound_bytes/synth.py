"""Waveform generation for the three chip-style voices: pulse, triangle, noise."""
from __future__ import annotations

from typing import Dict, List

import numpy as np

from .parser import Instrument, Note

# Drum presets for noise channels: sample-and-hold rate (Hz), decay time constant (s), level.
DRUM_PRESETS: Dict[str, Dict[str, float]] = {
    "K": {"rate": 1200.0, "decay": 0.05, "level": 1.0},
    "S": {"rate": 9000.0, "decay": 0.06, "level": 0.8},
    "H": {"rate": 24000.0, "decay": 0.015, "level": 0.5},
}


def midi_to_freq(midi: int) -> float:
    return 440.0 * 2.0 ** ((midi - 69) / 12.0)


def _adsr(n: int, sr: int, attack: float, decay: float, sustain: float, release: float) -> np.ndarray:
    """Simple ADSR envelope of exactly n samples; the release is folded into the note's tail."""
    t = np.arange(n) / sr
    env = np.ones(n)
    if attack > 0:
        env = np.minimum(env, t / attack)
    if decay > 0:
        after = np.clip((t - attack) / decay, 0.0, 1.0)
        env = env * (1.0 - after * (1.0 - sustain))
    else:
        env = env * np.where(t >= attack, sustain, 1.0)
    if release > 0:
        env = env * np.minimum(1.0, (n / sr - t) / release)
    return env


def _pulse(freq: float, n: int, sr: int, duty: float) -> np.ndarray:
    phase = (np.arange(n) * freq / sr) % 1.0
    return np.where(phase < duty, 1.0, -1.0) - (2.0 * duty - 1.0)  # remove DC offset so low end stays clean


def _triangle(freq: float, n: int, sr: int) -> np.ndarray:
    phase = (np.arange(n) * freq / sr) % 1.0
    tri = 4.0 * np.abs(phase - 0.5) - 1.0
    # Quantize to 16 levels, like the 4-bit triangle channel on the NES.
    return np.round((tri + 1.0) * 7.5) / 7.5 - 1.0


def _noise(rate: float, n: int, sr: int, rng: np.random.Generator) -> np.ndarray:
    steps = int(n * rate / sr) + 2
    values = rng.choice([-1.0, 1.0], size=steps)
    return values[(np.arange(n) * rate / sr).astype(int)]


def _voice(inst: Instrument, freq: float, n: int, sr: int) -> np.ndarray:
    p = inst.params
    if inst.wave == "pulse":
        return _pulse(freq, n, sr, p.get("duty", 0.5))
    return _triangle(freq, n, sr)


def _drum(drum: str, n: int, sr: int, rng: np.random.Generator) -> np.ndarray:
    preset = DRUM_PRESETS[drum]
    t = np.arange(n) / sr
    noise = _noise(preset["rate"], n, sr, rng) * np.exp(-t / preset["decay"])
    if drum == "K":  # pitch-dropping sine thump + a little noise click
        phase = np.cumsum(45.0 + 110.0 * np.exp(-t / 0.035)) / sr
        return (0.9 * np.sin(2 * np.pi * phase) * np.exp(-t / 0.14) + 0.3 * noise) * preset["level"]
    if drum == "S":  # noise + short tonal body
        return (noise + 0.35 * np.sin(2 * np.pi * 190.0 * t) * np.exp(-t / 0.05)) * preset["level"]
    return noise * preset["level"]


def render_note(inst: Instrument, note: Note, n: int, sr: int, rng: np.random.Generator) -> np.ndarray:
    """Render one note into n samples (n is the full slot length)."""
    p = inst.params
    volume = p.get("volume", 0.5)
    if n <= 0 or note.kind == "rest":
        return np.zeros(max(n, 0))

    if note.kind == "drum":
        return _drum(note.drum, n, sr, rng) * volume

    freq = midi_to_freq(note.midi)
    detune = p.get("detune", 0.0)  # cents; two voices detuned either side of the pitch for a thicker, chorused tone
    if detune > 0:
        spread = 2.0 ** (detune / 1200.0)
        wave = 0.5 * (_voice(inst, freq * spread, n, sr) + _voice(inst, freq / spread, n, sr))
    else:
        wave = _voice(inst, freq, n, sr)
    sub = p.get("sub", 0.0)  # level of a sine one octave below, for low-end weight
    if sub > 0:
        wave = (wave + sub * np.sin(2 * np.pi * (np.arange(n) * freq / 2.0 / sr))) / (1.0 + 0.5 * sub)
    env = _adsr(
        n, sr,
        attack=p.get("attack", 0.005),
        decay=p.get("decay", 0.0),
        sustain=p.get("sustain", 1.0),
        release=p.get("release", 0.02),
    )
    return wave * env * volume


def render_channel(inst: Instrument, notes: List[Note], tempo: float, sr: int, seed: int = 0) -> np.ndarray:
    """Render a whole channel. Note starts are computed from cumulative beats so timing never drifts."""
    rng = np.random.default_rng(seed)
    seconds_per_beat = 60.0 / tempo
    bounds = [0]
    total_beats = 0.0
    for note in notes:
        total_beats += note.beats
        bounds.append(int(round(total_beats * seconds_per_beat * sr)))
    out = np.zeros(bounds[-1])
    for note, start, end in zip(notes, bounds, bounds[1:]):
        out[start:end] = render_note(inst, note, end - start, sr, rng)
    return _echo(out, inst.params.get("echo", 0.0), seconds_per_beat, sr)


def _echo(dry: np.ndarray, amount: float, seconds_per_beat: float, sr: int) -> np.ndarray:
    """Tempo-synced (dotted eighth) three-tap echo for depth. Length is unchanged so stems stay aligned."""
    if amount <= 0:
        return dry
    delay = int(round(0.375 * seconds_per_beat * sr))
    out = dry.copy()
    for k in (1, 2, 3):
        d = k * delay
        if 0 < d < len(dry):
            out[d:] += dry[:-d] * amount * 0.5 ** k
    return out

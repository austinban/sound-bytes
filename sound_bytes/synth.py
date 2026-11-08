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


def _phase(freq_t: np.ndarray, sr: int) -> np.ndarray:
    """Oscillator phase (0..1) for a per-sample frequency curve; starts at 0, so a constant freq is just i*f/sr."""
    return ((np.cumsum(freq_t) - freq_t) / sr) % 1.0


def _pulse(phase: np.ndarray, duty) -> np.ndarray:
    """duty may be a number or a per-sample array (pulse-width modulation)."""
    return np.where(phase < duty, 1.0, -1.0) - (2.0 * duty - 1.0)  # remove DC offset so low end stays clean


def _triangle(phase: np.ndarray) -> np.ndarray:
    tri = 4.0 * np.abs(phase - 0.5) - 1.0
    # Quantize to 16 levels, like the 4-bit triangle channel on the NES.
    return np.round((tri + 1.0) * 7.5) / 7.5 - 1.0


def _noise(rate: float, n: int, sr: int, rng: np.random.Generator) -> np.ndarray:
    steps = int(n * rate / sr) + 2
    values = rng.choice([-1.0, 1.0], size=steps)
    return values[(np.arange(n) * rate / sr).astype(int)]


def _voice(inst: Instrument, freq_t: np.ndarray, sr: int, duty, t: np.ndarray) -> np.ndarray:
    p = inst.params
    phase = _phase(freq_t, sr)
    wave = inst.wave
    if wave == "pulse":
        return _pulse(phase, duty)
    if wave == "saw":
        return 2.0 * phase - 1.0
    if wave == "sine":
        return np.sin(2 * np.pi * phase)
    if wave == "organ":  # four drawbars: fundamental + 2nd, 3rd, 4th harmonics
        tau = 2 * np.pi * phase
        return (np.sin(tau) + 0.6 * np.sin(2 * tau) + 0.4 * np.sin(3 * tau) + 0.25 * np.sin(4 * tau)) / 2.25
    if wave == "fm":  # two-operator FM; the modulation index decays, which gives bells / electric pianos their attack
        index = p.get("index", 2.0) * np.exp(-t / max(p.get("index_decay", 0.3), 1e-3))
        mod = _phase(freq_t * p.get("ratio", 2.0), sr)
        return np.sin(2 * np.pi * phase + index * np.sin(2 * np.pi * mod))
    return _triangle(phase)


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

    t = np.arange(n) / sr
    # --- pitch curve (in cents): vibrato LFO that fades in after a delay, plus a glide into the note
    cents = np.zeros(n)
    vib = p.get("vibrato", 0.0)  # peak depth in cents
    if vib > 0:
        ramp = np.clip((t - p.get("vibrato_delay", 0.15)) / 0.1, 0.0, 1.0)
        cents += vib * ramp * np.sin(2 * np.pi * p.get("vibrato_rate", 5.5) * t)
    slide = p.get("slide", 0.0)  # start this many semitones above (negative: below), gliding to the real pitch
    if slide:
        cents += slide * 100.0 * np.exp(-t / max(p.get("slide_time", 0.08), 1e-3))
    freq_t = midi_to_freq(note.midi) * 2.0 ** (cents / 1200.0)

    duty = p.get("duty", 0.5)
    pwm = p.get("pwm", 0.0)  # pulse-width modulation depth: the duty cycle swings +/- pwm around `duty`
    if pwm > 0:
        duty = np.clip(duty + pwm * np.sin(2 * np.pi * p.get("pwm_rate", 2.0) * t), 0.05, 0.95)

    detune = p.get("detune", 0.0)  # cents; two voices detuned either side of the pitch for a thicker, chorused tone
    if detune > 0:
        spread = 2.0 ** (detune / 1200.0)
        wave = 0.5 * (_voice(inst, freq_t * spread, sr, duty, t) + _voice(inst, freq_t / spread, sr, duty, t))
    else:
        wave = _voice(inst, freq_t, sr, duty, t)
    sub = p.get("sub", 0.0)  # level of a sine one octave below, for low-end weight
    if sub > 0:
        wave = (wave + sub * np.sin(2 * np.pi * _phase(freq_t / 2.0, sr))) / (1.0 + 0.5 * sub)
    env = _adsr(
        n, sr,
        attack=p.get("attack", 0.005),
        decay=p.get("decay", 0.0),
        sustain=p.get("sustain", 1.0),
        release=p.get("release", 0.02),
    )
    trem = p.get("tremolo", 0.0)  # volume wobble depth 0..1
    if trem > 0:
        env = env * (1.0 - trem * 0.5 * (1.0 - np.cos(2 * np.pi * p.get("tremolo_rate", 6.0) * t)))
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

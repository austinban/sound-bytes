"""Sound-effect library: every sfx/<category>/<name>.sb is a tiny score with a metadata header.

Header lines (all comments, so the .sb stays a valid score):
    # desc:    what the sound is and what it sounds like
    # use:     when a game should trigger it
    # tags:    comma-separated search keywords
    # palette: pure | corrupted | neutral
    # zone:    any | sanctuary | hollow-wood | weeping-marsh | ashen-citadel | crystal-depths | rotted-heart
    # fit:     core | usable | off-theme   (how well it suits an eerie corrupted spirit realm)
    # loop:    N   (seconds; present only for loops: the file is rendered to wrap seamlessly)

    python3 -m sound_bytes.sfx --out out/sfx            # render every sound to WAV
    python3 -m sound_bytes.sfx --out out/sfx --format both
    python3 -m sound_bytes.sfx --catalog                # rewrite sfx/catalog.json and sfx/CATALOG.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np

from .parser import parse_score
from .render import mix, render_score, write_mp3, write_wav
from .songio import midi_to_name, score_to_json

SFX_DIR = Path(__file__).resolve().parent.parent / "sfx"
_PART_RE = re.compile(r"^[A-Za-z0-9_-]+$")
SAMPLE_RATE = 44100
META_KEYS = ("desc", "use", "tags", "palette", "zone", "fit", "loop")


def read_meta(text: str) -> Dict[str, str]:
    meta = {}
    for key in META_KEYS:
        m = re.search(rf"^#\s*{key}:\s*(.+)$", text, re.MULTILINE)
        if m:
            meta[key] = m.group(1).strip()
    return meta


def load_taxonomy(root: Path = SFX_DIR) -> Dict[str, Any]:
    path = root / "taxonomy.json"
    return json.loads(path.read_text()) if path.is_file() else {}


def _sound_paths(root: Path = SFX_DIR) -> List[Path]:
    return sorted(root.glob("*/*.sb"))


def wrap_loop(samples: np.ndarray, fade_s: float, sr: int) -> np.ndarray:
    """Seamless loop: overlap the faded-out tail onto the faded-in head, then drop the tail."""
    x = int(fade_s * sr)
    if x <= 0 or len(samples) <= 2 * x:
        return samples
    out = samples[:-x].copy()
    out[:x] += samples[-x:]
    peak = float(np.max(np.abs(out)))
    return out * (0.95 / peak) if peak > 0.95 else out


def list_sfx(root: Path = SFX_DIR) -> List[Dict[str, Any]]:
    """Every sound with its metadata and the note data the browser synth needs."""
    sounds = []
    for path in _sound_paths(root):
        text = path.read_text()
        score = parse_score(text)
        meta = read_meta(text)
        song = score_to_json(score)
        beats = max((sum(n.beats for n in notes) for notes in score.channels.values()), default=0.0)
        song["beats"] = beats
        loop = float(meta.get("loop", 0) or 0)
        sounds.append({
            "id": f"{path.parent.name}/{path.stem}",
            "category": path.parent.name,
            "name": path.stem,
            "title": score.title,
            "description": meta.get("desc", ""),
            "use_when": meta.get("use", ""),
            "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
            "palette": meta.get("palette", "neutral"),
            "zone": meta.get("zone", "any"),
            "fit": meta.get("fit", "usable"),
            "loop": loop,
            "seconds": beats * 60.0 / score.tempo - loop,
            "song": song,
        })
    return sounds


def find_sfx(category: str, name: str, root: Path = SFX_DIR) -> Optional[Path]:
    """Resolve an id to a file, refusing anything but plain names (no path tricks)."""
    if not (_PART_RE.match(category) and _PART_RE.match(name)):
        return None
    path = root / category / f"{name}.sb"
    return path if path.is_file() else None


def render_sfx(path: Path, sr: int = SAMPLE_RATE) -> np.ndarray:
    text = path.read_text()
    samples = mix(render_score(parse_score(text), sr))
    loop = float(read_meta(text).get("loop", 0) or 0)
    return wrap_loop(samples, loop, sr) if loop else samples


def render_all(out_dir: Path, formats=("wav",), sr: int = SAMPLE_RATE, root: Path = SFX_DIR) -> int:
    count = 0
    for path in _sound_paths(root):
        target = out_dir / path.parent.name
        target.mkdir(parents=True, exist_ok=True)
        samples = render_sfx(path, sr)
        for fmt in formats:
            if fmt == "wav":
                write_wav(target / f"{path.stem}.wav", samples, sr)
            else:
                write_mp3(target / f"{path.stem}.mp3", samples, sr)
        count += 1
    return count


# ---------------------------------------------------------------- catalog (for people and bots reading the repo)
_VOICE = {"pulse": "pulse wave", "triangle": "triangle wave", "saw": "sawtooth", "sine": "sine", "fm": "FM bell/e-piano tone",
          "organ": "organ", "noise": "noise"}


def _profile(path: Path, score, samples: np.ndarray, sr: int, loop: float) -> Dict[str, Any]:
    """Objective description of what the audio actually is, computed from the score and the rendered samples."""
    spec = np.abs(np.fft.rfft(samples * np.hanning(len(samples)))) ** 2
    freqs = np.fft.rfftfreq(len(samples), 1 / sr)
    total = float(spec.sum()) or 1.0
    centroid = float((freqs * spec).sum() / total)
    low = float(spec[freqs < 100].sum() / total)
    seconds = len(samples) / sr
    params = [inst.params for inst in score.instruments.values()]
    waves = sorted({inst.wave for inst in score.instruments.values()}, key=list(_VOICE).index)
    midis = [n.midi for notes in score.channels.values() for n in notes
             if n.kind == "pitch" and score.instruments[next(k for k, v in score.channels.items() if v is notes)].wave != "noise"]
    brightness = ("very dark" if centroid < 400 else "dark" if centroid < 900 else "mid" if centroid < 2000
                  else "bright" if centroid < 4000 else "very bright")
    weight = "bass-heavy" if low > 0.5 else "bass-present" if low > 0.25 else "light low end"
    length = "tick" if seconds < 0.15 else "short" if seconds < 0.5 else "medium" if seconds < 1.5 else "long"
    traits = []
    if any(p.get("slide", 0) > 0 for p in params): traits.append("pitch falls")
    if any(p.get("slide", 0) < 0 for p in params): traits.append("pitch rises")
    if any(p.get("vibrato", 0) > 0 for p in params): traits.append("vibrato")
    if any(p.get("tremolo", 0) > 0 for p in params): traits.append("tremolo pulsing")
    if any(p.get("pwm", 0) > 0 for p in params): traits.append("sweeping pulse width")
    if any(p.get("detune", 0) > 0 for p in params): traits.append("detuned/chorused")
    if any(p.get("echo", 0) > 0 for p in params): traits.append("echoing tail")
    if any(p.get("bits", 0) > 0 or p.get("hold", 1) > 1 for p in params): traits.append("bitcrushed")
    if "noise" in waves: traits.append("noisy/breathy")
    prof = {
        "voices": [_VOICE[w] for w in waves],
        "pitch_range": [midi_to_name(min(midis)), midi_to_name(max(midis))] if midis else None,
        "brightness": brightness,
        "low_end": weight,
        "length": length,
        "traits": traits,
        "peak_level": round(float(np.max(np.abs(samples))), 2),
    }
    prof["summary"] = (f"{length.capitalize()} ({seconds:.2f}s{', loops seamlessly' if loop else ''}), {brightness}, {weight}; "
                       f"voices: {', '.join(prof['voices'])}" + (f"; {', '.join(traits)}" if traits else "") + ".")
    return prof


def build_catalog(root: Path = SFX_DIR, sr: int = 22050) -> Dict[str, Any]:
    taxonomy = load_taxonomy(root)
    cats = taxonomy.get("categories", {})
    sounds = []
    for path in _sound_paths(root):
        text = path.read_text()
        score = parse_score(text)
        meta = read_meta(text)
        loop = float(meta.get("loop", 0) or 0)
        samples = render_sfx(path, sr)
        cat = path.parent.name
        sounds.append({
            "id": f"{cat}/{path.stem}",
            "file": f"sfx/{cat}/{path.stem}.sb",
            "title": score.title,
            "category": cat,
            "category_label": cats.get(cat, {}).get("label", cat),
            "description": meta.get("desc", ""),
            "use_when": meta.get("use", ""),
            "palette": meta.get("palette", "neutral"),
            "zone": meta.get("zone", "any"),
            "theme_fit": meta.get("fit", "usable"),
            "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
            "loop": {"seamless": True, "fade_seconds": loop} if loop else None,
            "duration_seconds": round(len(samples) / sr, 2),
            "profile": _profile(path, score, samples, sr, loop),
        })
    return {
        "about": ("Machine-readable index of the sound-effect library for an eerie, corrupted spirit-realm RPG. Each entry's "
                  "`file` is a tiny chiptune-style score (see README.md) that renders to audio with `python3 -m sound_bytes.sfx`. "
                  "`description` says what the sound is and what it sounds like; `use_when` says when a game should play it; "
                  "`profile` is measured from the rendered audio."),
        "regenerate": "python3 -m sound_bytes.sfx --catalog",
        "taxonomy": taxonomy,
        "count": len(sounds),
        "sounds": sounds,
    }


def catalog_markdown(cat: Dict[str, Any]) -> str:
    tx = cat["taxonomy"]
    out = ["# Sound-effect catalog", "",
           f"{cat['count']} sounds for an eerie, corrupted spirit-realm RPG. This file is generated from the `.sb` headers and "
           f"the rendered audio (`{cat['regenerate']}`); the same data is in `catalog.json`. Each sound is a tiny script in "
           "`sfx/<category>/<name>.sb`.", "", "## How to read an entry", "",
           "- **Description**: what the sound is and what it sounds like.", "- **Use when**: when a game should trigger it.",
           "- **Palette / Zone / Theme fit**: see the sections below.",
           "- **Sonic profile**: measured from the rendered audio (brightness, bass weight, length, voices, motion).", ""]
    for title, key in (("Palettes", "palettes"), ("Zones", "zones"), ("Theme fit", "theme_fit")):
        if tx.get(key):
            out += [f"## {title}", ""] + [f"- **{k}**: {v if isinstance(v, str) else v.get('description', '')}"
                                          if key != "zones" else f"- **{k}** ({v['name']}): {v['description']}"
                                          for k, v in tx[key].items()] + [""]
    if tx.get("loops"):
        out += ["## Loops", "", tx["loops"], ""]
    by_cat: Dict[str, list] = {}
    for s in cat["sounds"]:
        by_cat.setdefault(s["category"], []).append(s)
    for c, items in by_cat.items():
        info = tx.get("categories", {}).get(c, {})
        out += [f"## {info.get('label', c)} (`{c}`)", "", info.get("description", ""), ""]
        for s in items:
            loop = f" · loops seamlessly (fade {s['loop']['fade_seconds']}s)" if s["loop"] else ""
            out += [f"### `{s['id']}` — {s['title']}", "",
                    f"- **Description:** {s['description']}", f"- **Use when:** {s['use_when']}",
                    f"- **Palette:** {s['palette']} · **Zone:** {s['zone']} · **Theme fit:** {s['theme_fit']} · "
                    f"**Duration:** {s['duration_seconds']}s{loop}",
                    f"- **Sonic profile:** {s['profile']['summary']}",
                    f"- **Tags:** {', '.join(s['tags'])}", f"- **File:** `{s['file']}`", ""]
    return "\n".join(out)


def write_catalog(root: Path = SFX_DIR) -> Dict[str, Any]:
    cat = build_catalog(root)
    (root / "catalog.json").write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n")
    (root / "CATALOG.md").write_text(catalog_markdown(cat))
    return cat


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Render the sound-effect library, or rebuild its catalog.")
    ap.add_argument("--out", type=Path, default=Path("out/sfx"))
    ap.add_argument("--format", choices=("wav", "mp3", "both"), default="wav")
    ap.add_argument("--catalog", action="store_true", help="rewrite sfx/catalog.json and sfx/CATALOG.md instead of rendering audio")
    args = ap.parse_args(argv)
    if args.catalog:
        cat = write_catalog()
        print(f"wrote sfx/catalog.json and sfx/CATALOG.md ({cat['count']} sounds)")
        return 0
    formats = ("wav", "mp3") if args.format == "both" else (args.format,)
    try:
        n = render_all(args.out, formats)
    except RuntimeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(f"rendered {n} sounds to {args.out}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

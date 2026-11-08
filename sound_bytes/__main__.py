"""CLI: python -m sound_bytes songs/demo.sb -o out/demo"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .parser import ScoreError, parse_score
from .render import render_to_dir


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sound_bytes", description="Render a .sb score to per-instrument WAV stems + a mix.")
    ap.add_argument("score", type=Path, help="path to a .sb score file")
    ap.add_argument("-o", "--out", type=Path, default=Path("out"), help="output directory (default: out)")
    ap.add_argument("--sample-rate", type=int, default=44100)
    ap.add_argument("--bit-depth", type=int, choices=(8, 16), default=16)
    ap.add_argument("--format", choices=("wav", "mp3", "both"), default="wav", help="output file format (mp3 needs: pip install lameenc)")
    ap.add_argument("--mp3-bitrate", type=int, default=192, help="MP3 bitrate in kbps (default 192)")
    args = ap.parse_args(argv)

    try:
        score = parse_score(args.score.read_text())
    except (OSError, ScoreError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    formats = ("wav", "mp3") if args.format == "both" else (args.format,)
    try:
        paths = render_to_dir(score, args.out, args.sample_rate, args.bit_depth, formats, args.mp3_bitrate)
    except RuntimeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(f"{score.title} @ {score.tempo:g} bpm")
    for name, files in paths.items():
        print(f"  {name:>8} -> {', '.join(str(f) for f in files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

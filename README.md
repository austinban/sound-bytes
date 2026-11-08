# sound-bytes

Write old-school 8-bit songs as text scripts, then render every instrument as its own WAV (plus a full mix).

## Piano-roll editor (browser)

    python3 -m sound_bytes.server        # opens http://127.0.0.1:8765/

Pick a song, click the grid to add notes (drag to set length, click a note to delete), choose an instrument per
track, mute/solo, play with Space, save with Cmd/Ctrl+S. "Render WAVs" saves, then writes per-instrument WAVs with
the Python renderer. Instruments are the JSON files in `instruments/` — drop in your own; in a script you can use
them as `instrument lead: @pulse-lead volume=0.4`. The server only listens on localhost.

## Command-line rendering

    pip install -r requirements.txt
    python3 -m sound_bytes songs/demo.sb -o out/demo      # add --bit-depth 8 for true 8-bit WAVs
    python3 -m sound_bytes songs/demo.sb -o out/demo --format mp3   # or --format both; --mp3-bitrate 256
    afplay out/demo/mix.wav                                # macOS; or open any file in out/demo/

Output: one `<instrument>.wav` (or `.mp3`) per channel (all the same length, so they line up in a DAW) and `mix.wav`.

## Script format

    title: Demo Quest
    tempo: 150
    instrument lead:  pulse duty=0.25 volume=0.55 attack=0.005 decay=0.08 sustain=0.7 release=0.04
    instrument bass:  triangle volume=0.6
    instrument drums: noise volume=0.6

    lead:  G5:1 G5:0.5 Eb5:0.5 R:1
    bass:  [C3:0.5 C3:0.5 C4:0.5 C3:0.5]x2
    drums: [K:1 H:0.5 H:0.5 S:1 H:0.5 K:0.5]x2

- Notes are `NAME:BEATS` (`C#4:0.5`); `R` is a rest. Lines for the same channel are joined in order.
- Voices: `pulse` (`duty` 0.125 / 0.25 / 0.5), `triangle`, `saw`, `sine`, `fm` (`ratio`, `index`, `index_decay` for bells and
  electric pianos), `organ` (drawbars), and `noise` (drums `K` kick, `S` snare, `H` hat). Pick a track's voice in the editor,
  or start from a preset in `instruments/`.
- Sound curves (any melodic voice): `vibrato` (cents) + `vibrato_rate`/`vibrato_delay`, `slide` (semitones, glides into each
  note) + `slide_time`, `pwm` + `pwm_rate` (pulse-width sweep), `tremolo` + `tremolo_rate`; plus `sub`, `detune`, `echo`.
- Optional params: `volume`, `attack`, `decay`, `sustain` (0-1), `release` (seconds).
- `[ ... ]xN` repeats; `#` starts a comment.

## Tests

    python3 -m unittest discover -s tests

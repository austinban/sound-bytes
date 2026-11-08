# Sound-effect library

About 230 short game sounds for an **eerie, corrupted spirit-realm RPG**, written as tiny chiptune-style scripts that render to audio.

**For a step-by-step guide (finding, choosing and rendering sounds, plus a game-event mapping) see [`../SOUND_EFFECTS_GUIDE.md`](../SOUND_EFFECTS_GUIDE.md).**
If you are a program or a person looking for a sound, start with [`catalog.json`](catalog.json)** (machine-readable) or
[`CATALOG.md`](CATALOG.md) (the same data as text). Every entry says what the sound is and what it sounds like (`description`),
when a game should play it (`use_when`), plus tags, palette, zone, theme fit, loop info, duration and a measured sonic profile.

## Layout

```
sfx/
  catalog.json        index of every sound (generated)
  CATALOG.md          the same index as readable text (generated)
  taxonomy.json       definitions of the categories, palettes, zones and theme-fit values
  <NN-category>/<name>.sb   one sound per file
```

Categories: `01-ui`, `02-items`, `03-movement`, `04-combat`, `05-magic`, `06-explosions`, `07-damage`, `08-environment`,
`09-battle`, `10-jingles` (the general set), then the spirit-realm set: `11-spirit`, `12-rpg-ui`, `13-status`, `14-spells`,
`15-enemies`, `16-realm`, `17-zones`, `18-corrupted`.

## The sound-design rules

- **Palettes.** `pure` = spirit light: clean bells, organ and sine tones, open fifths and major thirds (healing, cleansing,
  the player's own spirit powers, the sanctuary). `corrupted` = things gone wrong: detuned and inharmonic tones, tritones and
  minor seconds, tremolo wobble, bitcrush, long echoes (enemies, curses, corrupted zones). `neutral` = general sounds. The
  contrast lets players hear whether something is safe or dangerous.
- **Zones.** `sanctuary` (The Veil Haven, safe hub), `hollow-wood` (dead forest), `weeping-marsh` (flooded wetland),
  `ashen-citadel` (ruined stone city), `crystal-depths` (resonant crystal caverns), `rotted-heart` (source of the corruption).
  Each zone has an ambience loop (`amb-<zone>`), an entry sting (`enter-<zone>`) and one-shots.
- **Theme fit.** `core` = made for this setting, `usable` = generic, `off-theme` = arcade, sci-fi or modern flavour
  (guns, lasers, countdowns); avoid those here unless contrast is deliberate.
- **Variants.** Sounds that repeat often come in numbered variants (`corrupted-footstep-1..3`, `whisper-1..3`,
  `crystal-chime-1..3`); a game should pick randomly among them.
- **Loops.** Entries with a `loop` value (the `amb-*` sounds) are rendered to wrap seamlessly: the faded tail is overlapped onto
  the head. Play them with looping on; do not add a crossfade. `duration_seconds` is the loop length.
- **Corrupted counterparts** of classic sounds live in `18-corrupted` (for example `soul-shard` replaces `coin`).

## The `.sb` header

Every sound is a valid score (see the top-level README for the note format) with a metadata header made of comments:

```
title: Soul Shard
tempo: 120
# desc:    what the sound is and what it sounds like
# use:     when a game should trigger it
# tags:    comma, separated, keywords
# palette: pure | corrupted | neutral
# zone:    any | sanctuary | hollow-wood | weeping-marsh | ashen-citadel | crystal-depths | rotted-heart
# fit:     core | usable | off-theme
# loop:    0.5      (only for loops: the fade length in seconds)
```

## Use it

```bash
python3 -m sound_bytes.server                      # browse and click-to-play at http://127.0.0.1:8765/sfx.html
python3 -m sound_bytes.sfx --out out/sfx           # render every sound to WAV (add --format both for MP3 too)
python3 -m sound_bytes.sfx --catalog               # rebuild catalog.json and CATALOG.md after editing any .sb
```

To add a sound, put a new `.sb` in a category folder with the header above, then rebuild the catalog. The tests fail if the
catalog is out of date or a header is invalid (`python3 -m unittest discover -s tests`).

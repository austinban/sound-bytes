# Sound-effect library: guide for bots and tools

This repo holds **227 short game sounds for an eerie, corrupted spirit-realm RPG**. They are not stored as audio files. Each
sound is a tiny text script that this repo renders to audio on demand. Everything you need to *find*, *choose* and *get* a sound
is below.

## In 30 seconds

1. **Find a sound:** read [`sfx/catalog.json`](sfx/catalog.json). Each entry says what the sound is, what it sounds like and when to use it.
2. **Pick it:** filter by `zone`, `palette`, `theme_fit` and `tags`, or use the event table below.
3. **Get the audio:** run `python3 -m sound_bytes.sfx --out out/sfx` (all sounds, WAV), or render one sound with the snippet in "Getting audio".

## Where things are

| Path | What it is |
| --- | --- |
| [`sfx/catalog.json`](sfx/catalog.json) | **Start here.** Every sound with descriptions, tags and a measured sonic profile (machine-readable). |
| [`sfx/CATALOG.md`](sfx/CATALOG.md) | The same catalog as readable text, grouped by category. |
| [`sfx/taxonomy.json`](sfx/taxonomy.json) | Definitions of every category, palette, zone and theme-fit value. |
| `sfx/<category>/<name>.sb` | The sound itself: one tiny script per sound, with a metadata header. |
| [`sfx/README.md`](sfx/README.md) | The sound-design rules and the `.sb` header format. |
| `out/sfx/<category>/<name>.wav` | Rendered audio. **Created by you** when you run the renderer; not in git. |
| [`web/sfx.html`](web/sfx.html) | A click-to-play browser page for humans (served by `python3 -m sound_bytes.server`). |

A sound's **id** is `<category>/<name>`, for example `18-corrupted/soul-shard`. Its file is `sfx/<id>.sb` and, once rendered,
`out/sfx/<id>.wav`.

## Anatomy of a catalog entry

```json
{
  "id": "18-corrupted/soul-shard",
  "file": "sfx/18-corrupted/soul-shard.sb",
  "title": "Soul Shard",
  "category": "18-corrupted",
  "description": "Currency pickup, corrupted: a detuned, inharmonic two-note ring with a crushed edge.",
  "use_when": "Collecting soul shards (the realm's currency). Replaces coin in this setting.",
  "palette": "corrupted",
  "zone": "any",
  "theme_fit": "core",
  "tags": ["corrupted", "soul", "shard", "currency", "pickup", "soul shard", "coin replacement"],
  "loop": null,
  "duration_seconds": 1.06,
  "profile": { "summary": "Medium (1.06s), very bright, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail, bitcrushed." }
}
```

- `description`: what it is and what it sounds like. `use_when`: the game event that should trigger it.
- `profile`: measured from the rendered audio (brightness, bass weight, length, voices, pitch motion). It is objective; `description` is the author's intent.
- `loop`: `null` for one-shots. For ambience loops it is `{"seamless": true, "fade_seconds": 0.5}` (see "Playing them").
- `duration_seconds`: for a loop, this is the loop length.

## Choosing a sound

**Palettes** (the main design rule: players should be able to hear safe vs dangerous):
- `pure`: spirit light. Clean bells, organ and sine tones. Healing, cleansing, the player's own spirit powers, the sanctuary.
- `corrupted`: things gone wrong. Detuned, inharmonic, tritones, wobble, bitcrush, long echoes. Enemies, curses, corrupted zones.
- `neutral`: general sounds, tuned dark.

**Zones:** `sanctuary` (Veil Haven, safe hub), `hollow-wood` (dead forest), `weeping-marsh` (flooded wetland),
`ashen-citadel` (ruined stone city), `crystal-depths` (resonant crystal caverns), `rotted-heart` (source of the corruption).
`any` means the sound is not tied to a zone. Every zone has an ambience loop (`amb-<zone>`) and an entry sting (`enter-<zone>`).

**Theme fit:** `core` = made for this setting. `usable` = generic. `off-theme` = arcade, sci-fi or modern (guns, lasers,
countdowns, 1-ups): **do not use these in this setting** unless you want a deliberate contrast.

**Prefer the corrupted counterpart** inside the realm: `18-corrupted/` has corrupted versions of the classic pickup, movement
and UI sounds (for example `soul-shard` instead of `coin`). Classic entries name their counterpart in `use_when`.

```python
import json
catalog = json.load(open("sfx/catalog.json"))["sounds"]
# everything usable in the Weeping Marsh that fits the setting
marsh = [s["id"] for s in catalog if s["zone"] == "weeping-marsh" and s["theme_fit"] != "off-theme"]
# search by keyword across tags, description and use_when
heal = [s["id"] for s in catalog if "heal" in " ".join(s["tags"] + [s["description"], s["use_when"]]).lower()]
```

## Starter mapping: game event to sound id

Use these unless a more specific sound in the catalog fits better.

| Game event | Sound id(s) |
| --- | --- |
| Menu move / confirm / cancel / denied | `01-ui/cursor-move`, `01-ui/confirm`, `01-ui/cancel`, `01-ui/denied-buzz` |
| Dialogue text blip (low / high voice) | `01-ui/text-blip-low`, `01-ui/text-blip-high` |
| Notification, dialogue opens | `01-ui/notification-ping`, `12-rpg-ui/dialogue-open` |
| Save game (sanctuary / corrupted zone) | `01-ui/save-chime` or `16-realm/lantern-light` / `18-corrupted/corrupted-save` |
| Inventory open / close | `12-rpg-ui/inventory-open`, `12-rpg-ui/inventory-close` |
| Equip / unequip | `12-rpg-ui/item-equip`, `12-rpg-ui/item-unequip` |
| Potion, scroll | `12-rpg-ui/potion-use`, `12-rpg-ui/scroll-read` |
| Quest accepted / updated / completed | `12-rpg-ui/quest-accept`, `12-rpg-ui/quest-update`, `10-jingles/quest-complete` |
| Vendor buy / sell | `12-rpg-ui/trade-complete`, `18-corrupted/shard-spend` |
| Map, fast travel, skill unlock | `12-rpg-ui/map-open`, `12-rpg-ui/fast-travel`, `12-rpg-ui/skill-unlock` |
| Currency pickup (soul shards) | `18-corrupted/soul-shard` |
| Health / mana / key pickup | `18-corrupted/blighted-heart`, `18-corrupted/void-essence`, `18-corrupted/rusted-key` |
| Chest, relic, soul collected | `18-corrupted/tainted-treasure` or `16-realm/cursed-chest-open`, `16-realm/relic-pickup`, `11-spirit/soul-absorb` |
| Footsteps on corrupted ground (random of 3) | `18-corrupted/corrupted-footstep-1`, `-2`, `-3` (same folder) |
| Footstep on stone, jump, land, dash | `03-movement/footstep-stone`, `18-corrupted/corrupted-jump`, `18-corrupted/corrupted-land`, `03-movement/dash` |
| Melee swing / hit / heavy / critical | `04-combat/sword-swing`, `04-combat/sword-hit`, `04-combat/heavy-hit`, `04-combat/critical-hit` |
| Parry, shield block, enemy hurt | `04-combat/parry-clang`, `04-combat/shield-block`, `04-combat/enemy-hurt` |
| Enemy dies (spirit-type) | `15-enemies/vanish-into-smoke` |
| Player hurt / dies / game over | `07-damage/player-hurt`, `07-damage/player-death`, `07-damage/game-over` |
| Low health | `09-battle/low-health-heartbeat` (not the arcade `low-health-beep`) |
| Spells | `14-spells/soul-drain`, `spectral-blade`, `shadow-step`, `void-bolt`, `spirit-lance`, `exorcism`, `ward-barrier`, `barrier-break`, `ghostfire`, `gravity-well`, `plague-cloud` (all in `14-spells/`); `05-magic/heal-spell`, `05-magic/summon` |
| Status effect applied | `13-status/corrupted-applied`, `cursed-applied`, `drained-applied`, `silenced-applied`, `rooted-applied`, `fear-applied`, `blessed-applied` (all in `13-status/`) |
| Status tick / wears off | `13-status/bleed-tick`, `11-spirit/corruption-tick`, `13-status/status-expire` |
| Spirit form / spirit sight | `11-spirit/spirit-form-on`, `11-spirit/spirit-form-off`, `11-spirit/spirit-sight-on`, `11-spirit/spirit-sight-off` |
| Possession, banish, bind, purify | `11-spirit/possession-start`, `11-spirit/possession-end`, `11-spirit/banish`, `11-spirit/soul-bind`, `11-spirit/purify-cleanse` |
| Corruption spreads | `11-spirit/corruption-spread` |
| Haunted flavour (random of 3) | `11-spirit/whisper-1`, `-2`, `-3` (same folder) |
| Enemy voices | `15-enemies/wraith-wail`, `spectre-screech`, `undead-groan`, `bone-rattle`, `beast-growl`, `beast-snarl`, `cultist-chant` (all in `15-enemies/`) |
| Enemy spawn / shamble / swarm | `15-enemies/spawn-from-void`, `15-enemies/husk-shamble`, `15-enemies/swarm-skitter` |
| Battle starts | `09-battle/battle-start` |
| Boss intro / phase change / defeat | `15-enemies/boss-intro`, `15-enemies/boss-surge`, `15-enemies/boss-collapse` |
| Rift, shrine, gate, veil | `16-realm/rift-open`, `16-realm/rift-close`, `16-realm/shrine-activate`, `16-realm/spirit-gate-open`, `16-realm/veil-pass` |
| Crystals, lore tablet, relic hum | `16-realm/crystal-chime-1` (also `-2`, `-3`), `16-realm/lore-tablet`, `16-realm/relic-resonance` |
| Title, checkpoint, defeat, victory | `10-jingles/title-sting`, `10-jingles/checkpoint`, `10-jingles/defeat-sting`, `10-jingles/victory-fanfare` |
| Level up (normal / corrupted) | `10-jingles/level-up`, `18-corrupted/corrupted-level-up` |
| Enter a zone | `17-zones/enter-sanctuary`, `enter-hollow-wood`, `enter-weeping-marsh`, `enter-ashen-citadel`, `enter-crystal-depths`, `enter-rotted-heart` (all in `17-zones/`) |
| Zone background ambience (loop) | `17-zones/amb-sanctuary`, `amb-hollow-wood`, `amb-weeping-marsh`, `amb-ashen-citadel`, `amb-crystal-depths`, `amb-rotted-heart` (all in `17-zones/`) |

## Getting audio

Requires Python 3.9+ and `pip install -r requirements.txt` (numpy; `lameenc` only if you want MP3). Run from the repo root.

```bash
python3 -m sound_bytes.sfx --out out/sfx                  # all 227 sounds -> out/sfx/<category>/<name>.wav
python3 -m sound_bytes.sfx --out out/sfx --format both    # WAV and MP3 (192 kbps)
```

Render a single sound:

```python
from pathlib import Path
from sound_bytes.sfx import find_sfx, render_sfx, SAMPLE_RATE
from sound_bytes.render import write_wav

samples = render_sfx(find_sfx("18-corrupted", "soul-shard"))      # numpy float array, mono
write_wav(Path("soul-shard.wav"), samples, SAMPLE_RATE)
```

Or, with the server running (`python3 -m sound_bytes.server --port 8765`), fetch `GET /api/sfx` for the full catalog data and
`GET /api/sfx/<category>/<name>.wav` for one rendered WAV. It listens on `127.0.0.1` only.

**Output format:** mono, 44.1 kHz, 16-bit WAV (all 227 files are about 24 MB in total). Peak level is at most 0.95, so nothing
clips; levels are not normalised against each other, so set per-category volumes in your engine. Rendering is deterministic: the
same `.sb` always gives the same audio.

## Playing them

- **Variants:** sounds named `...-1`, `-2`, `-3` (`corrupted-footstep-*`, `whisper-*`, `crystal-chime-*`) are variants of one sound.
  Pick randomly, and avoid repeating the last one.
- **Loops:** only entries with a non-null `loop` (the six `amb-*` sounds) are loops. They already wrap seamlessly, so enable looping
  and add no crossfade. Everything else is a one-shot.
- **Zones:** on entering a zone, play its `enter-<zone>` sting once and start its `amb-<zone>` loop (fading out the previous loop).
- **Palettes:** use `pure` sounds for healing, cleansing, the sanctuary and the player's spirit powers, and `corrupted` sounds for
  enemies and corruption. Do not swap them: the contrast is the point.
- **Layering:** the sounds are short and synthesised, so they layer well. Keep ambience quiet and ducked under combat sounds, and
  keep sub-bass hits (`heavy-hit`, `explosion-*`, `boss-*`) from stacking on top of each other.

## Adding or changing a sound

Edit or add a `.sb` in `sfx/<category>/`. Keep the header (`# desc`, `# use`, `# tags`, `# palette`, `# zone`, `# fit`; see
[`sfx/README.md`](sfx/README.md)), then run `python3 -m sound_bytes.sfx --catalog` to refresh `catalog.json` and `CATALOG.md`.
`python3 -m unittest discover -s tests` fails if the catalog is stale, a header is invalid, or an id in this guide no longer exists.

## Limits

- **Synthesised chiptune-style audio only** (pulse, triangle, saw, sine, FM, organ and noise voices). No recordings, no voices or words.
- **Mono, short:** most one-shots are under 1.5 seconds and none is longer than 3.5 seconds; the six ambience loops are 11.5 seconds each.
- **Origin:** every sound and song here was generated from the scripts in this repo. The audio is synthesised; it contains no samples or recordings from any other source. No formal licence file has been added to the repo.

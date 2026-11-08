# Sound-effect catalog

227 sounds for an eerie, corrupted spirit-realm RPG. This file is generated from the `.sb` headers and the rendered audio (`python3 -m sound_bytes.sfx --catalog`); the same data is in `catalog.json`. Each sound is a tiny script in `sfx/<category>/<name>.sb`.

## How to read an entry

- **Description**: what the sound is and what it sounds like.
- **Use when**: when a game should trigger it.
- **Palette / Zone / Theme fit**: see the sections below.
- **Sonic profile**: measured from the rendered audio (brightness, bass weight, length, voices, motion).

## Palettes

- **pure**: Spirit-light sounds: clean bells, organ and sine tones in open fifths and major thirds. For healing, cleansing, the player's own spirit powers, and the sanctuary. They stand out against the corruption.
- **corrupted**: Sounds of things gone wrong: detuned and inharmonic tones (FM ratio of about 1.41), tritones and minor seconds, tremolo wobble, bitcrush, and long echoes. For enemies, corruption, curses and the darker zones.
- **neutral**: General game sounds with no palette; usable anywhere, but tuned dark.

## Zones

- **sanctuary** (The Veil Haven): Safe hub. Calm and warm; uses the pure palette (organ fifths, clean bells).
- **hollow-wood** (The Hollow Wood): Dead spirit forest of bone-white trees: dry wind, creaking, whispers, hollow wood.
- **weeping-marsh** (The Weeping Marsh): Flooded, corrupted wetland: slow drips, gloopy bubbles, heavy sodden low drones.
- **ashen-citadel** (The Ashen Citadel): Ruined stone city of ash: cavernous echo, distant tolling bells, grinding stone, cold wind.
- **crystal-depths** (The Crystal Depths): Caverns of resonant spirit crystal: glassy pings, shimmering hum, long echoes; mostly pure palette.
- **rotted-heart** (The Rotted Heart): The source of the corruption: heartbeat, huge dissonant drone, bitcrushed glitches, dread.

## Theme fit

- **core**: Designed for or well suited to an eerie, corrupted spirit realm.
- **usable**: Generic; fine to use, optionally re-pitched or paired with a corrupted variant.
- **off-theme**: Arcade, sci-fi or modern flavour (guns, lasers, countdowns...). Avoid in this setting unless it is a deliberate contrast.

## Loops

Sounds with a `loop` value are ambience loops. They are rendered to wrap seamlessly (the faded tail is overlapped onto the head), so play them with looping enabled and no extra crossfade. `duration_seconds` is the loop length.

## UI & menus (`01-ui`)

Menu and interface feedback.

### `01-ui/cancel` — Cancel

- **Description:** Back / cancel: the confirm gesture reversed.
- **Use when:** Backing out of a menu or dismissing a prompt.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.2s
- **Sonic profile:** Short (0.20s), mid, light low end; voices: pulse wave.
- **Tags:** ui, cancel, neutral
- **File:** `sfx/01-ui/cancel.sb`

### `01-ui/confirm` — Confirm

- **Description:** Menu selection accepted: a quick two-note rise.
- **Use when:** Accepting a menu choice or confirming a prompt.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.7s
- **Sonic profile:** Medium (0.70s), mid, light low end; voices: pulse wave; echoing tail.
- **Tags:** ui, confirm, neutral
- **File:** `sfx/01-ui/confirm.sb`

### `01-ui/cursor-move` — Cursor Move

- **Description:** Tiny blip when the cursor moves between menu items.
- **Use when:** Moving the cursor or selection between menu items.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.04s
- **Sonic profile:** Tick (0.04s), mid, light low end; voices: pulse wave.
- **Tags:** ui, cursor, move, neutral
- **File:** `sfx/01-ui/cursor-move.sb`

### `01-ui/denied-buzz` — Denied Buzz

- **Description:** Action not allowed: a low double buzz.
- **Use when:** An action is not allowed (cannot equip, not enough resources).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.32s
- **Sonic profile:** Short (0.32s), very dark, bass-present; voices: sawtooth; detuned/chorused.
- **Tags:** ui, denied, buzz, neutral
- **File:** `sfx/01-ui/denied-buzz.sb`

### `01-ui/menu-close` — Menu Close

- **Description:** Menu closing: a falling sweep.
- **Use when:** Closing a menu or panel.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.16s
- **Sonic profile:** Short (0.16s), mid, light low end; voices: pulse wave; pitch falls.
- **Tags:** ui, menu, close, neutral
- **File:** `sfx/01-ui/menu-close.sb`

### `01-ui/menu-open` — Menu Open

- **Description:** Menu sliding open: a rising sweep.
- **Use when:** Opening a menu or panel.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.2s
- **Sonic profile:** Short (0.20s), dark, light low end; voices: pulse wave; pitch rises.
- **Tags:** ui, menu, open, neutral
- **File:** `sfx/01-ui/menu-open.sb`

### `01-ui/notification-ping` — Notification Ping

- **Description:** Soft FM bell for a notification.
- **Use when:** A non-urgent notification, hint or journal update.
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 0.95s
- **Sonic profile:** Medium (0.95s), very bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** ui, notification, ping, pure
- **File:** `sfx/01-ui/notification-ping.sb`

### `01-ui/page-flip` — Page Flip

- **Description:** Quick paper-ish swish for turning pages.
- **Use when:** Turning a page in a book, journal or lore text.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.12s
- **Sonic profile:** Tick (0.12s), dark, light low end; voices: noise; pitch falls, noisy/breathy.
- **Tags:** ui, page, flip, neutral
- **File:** `sfx/01-ui/page-flip.sb`

### `01-ui/save-chime` — Save Chime

- **Description:** Game saved: a rising F minor bell figure.
- **Use when:** Confirming that the game was saved (pure palette: use at sanctuary).
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.24s
- **Sonic profile:** Medium (1.24s), very bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** ui, save, chime, pure
- **File:** `sfx/01-ui/save-chime.sb`

### `01-ui/scroll-tick` — Scroll Tick

- **Description:** Very short tick for scrolling a list.
- **Use when:** Each step while scrolling a long list.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.02s
- **Sonic profile:** Tick (0.02s), very dark, bass-heavy; voices: noise; noisy/breathy.
- **Tags:** ui, scroll, tick, neutral
- **File:** `sfx/01-ui/scroll-tick.sb`

### `01-ui/text-blip-high` — Text Blip High

- **Description:** Dialogue typewriter blip, high voice.
- **Use when:** Per-character blip for a high-voiced speaker's dialogue text.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.04s
- **Sonic profile:** Tick (0.04s), mid, light low end; voices: pulse wave.
- **Tags:** ui, text, blip, high, neutral
- **File:** `sfx/01-ui/text-blip-high.sb`

### `01-ui/text-blip-low` — Text Blip Low

- **Description:** Dialogue typewriter blip, low voice.
- **Use when:** Per-character blip for a deep-voiced speaker's dialogue text.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.04s
- **Sonic profile:** Tick (0.04s), dark, light low end; voices: pulse wave.
- **Tags:** ui, text, blip, low, neutral
- **File:** `sfx/01-ui/text-blip-low.sb`

### `01-ui/toggle-off` — Toggle Off

- **Description:** Switch flipped off.
- **Use when:** Disabling a setting or switch in a menu.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.12s
- **Sonic profile:** Tick (0.12s), mid, light low end; voices: pulse wave.
- **Tags:** ui, toggle, off, neutral
- **File:** `sfx/01-ui/toggle-off.sb`

### `01-ui/toggle-on` — Toggle On

- **Description:** Switch flipped on.
- **Use when:** Enabling a setting or switch in a menu.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.12s
- **Sonic profile:** Tick (0.12s), mid, light low end; voices: pulse wave.
- **Tags:** ui, toggle, on, neutral
- **File:** `sfx/01-ui/toggle-on.sb`

## Items & pickups (`02-items`)

Collecting and using items. Many have corrupted counterparts in 18-corrupted.

### `02-items/ammo-pickup` — Ammo Pickup

- **Description:** Mechanical clack for ammo or a clip.
- **Use when:** Picking up ammunition; arcade/sci-fi flavour, rarely needed in a spirit realm.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), mid, light low end; voices: pulse wave, noise; noisy/breathy.
- **Tags:** items, ammo, pickup, neutral
- **File:** `sfx/02-items/ammo-pickup.sb`

### `02-items/chest-open` — Chest Open

- **Description:** Creaking lid, then a sparkle of bells.
- **Use when:** Opening a treasure chest (see 16-realm/cursed-chest-open and 18-corrupted/tainted-treasure).
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.51s
- **Sonic profile:** Long (1.51s), very bright, light low end; voices: sawtooth, FM bell/e-piano tone; pitch rises, vibrato, echoing tail.
- **Tags:** items, chest, open, neutral
- **File:** `sfx/02-items/chest-open.sb`

### `02-items/coin-spend` — Coin Spend

- **Description:** Spending coins at a shop: a falling two-note pip.
- **Use when:** Paying currency at a shop (see 18-corrupted/shard-spend for the corrupted realm).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.15s
- **Sonic profile:** Short (0.15s), mid, light low end; voices: pulse wave.
- **Tags:** items, coin, spend, neutral
- **File:** `sfx/02-items/coin-spend.sb`

### `02-items/coin` — Coin

- **Description:** Classic coin pickup: two quick notes, the second rings out.
- **Use when:** Picking up currency in a bright or pure context (see 18-corrupted/soul-shard for the corrupted realm).
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 0.46s
- **Sonic profile:** Short (0.46s), bright, light low end; voices: pulse wave.
- **Tags:** items, coin, pure
- **File:** `sfx/02-items/coin.sb`

### `02-items/gem-pickup` — Gem Pickup

- **Description:** Sparkling crystal arpeggio on FM bells.
- **Use when:** Collecting a gem or crystal.
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 1.06s
- **Sonic profile:** Medium (1.06s), very bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** items, gem, pickup, pure
- **File:** `sfx/02-items/gem-pickup.sb`

### `02-items/heart-pickup` — Heart Pickup

- **Description:** Warm rising arpeggio for a health pickup.
- **Use when:** Picking up a health restore (see 18-corrupted/blighted-heart).
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 0.64s
- **Sonic profile:** Medium (0.64s), dark, light low end; voices: triangle wave; vibrato.
- **Tags:** items, heart, pickup, pure
- **File:** `sfx/02-items/heart-pickup.sb`

### `02-items/key-pickup` — Key Pickup

- **Description:** Bright metallic ring: you got a key.
- **Use when:** Obtaining a key (see 18-corrupted/rusted-key).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.46s
- **Sonic profile:** Short (0.46s), very bright, light low end; voices: FM bell/e-piano tone.
- **Tags:** items, key, pickup, neutral
- **File:** `sfx/02-items/key-pickup.sb`

### `02-items/mana-pickup` — Mana Pickup

- **Description:** Swirling pulse-width sweep for a mana pickup.
- **Use when:** Picking up a mana or energy restore (see 18-corrupted/void-essence).
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 0.85s
- **Sonic profile:** Medium (0.85s), mid, light low end; voices: pulse wave; pitch rises, sweeping pulse width, echoing tail.
- **Tags:** items, mana, pickup, pure
- **File:** `sfx/02-items/mana-pickup.sb`

### `02-items/one-up` — One Up

- **Description:** Extra life: a bouncy rising figure.
- **Use when:** Gaining an extra life; an arcade convention that does not suit this setting.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 1.25s
- **Sonic profile:** Medium (1.25s), bright, light low end; voices: pulse wave; echoing tail.
- **Tags:** items, one, up, neutral
- **File:** `sfx/02-items/one-up.sb`

### `02-items/power-up` — Power Up

- **Description:** Rising F minor run with vibrato on the last note.
- **Use when:** Gaining a temporary buff or upgrade (see 18-corrupted/corrupted-power-up).
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 1.25s
- **Sonic profile:** Medium (1.25s), bright, light low end; voices: pulse wave; vibrato, echoing tail.
- **Tags:** items, power, up, pure
- **File:** `sfx/02-items/power-up.sb`

### `02-items/treasure-found` — Treasure Found

- **Description:** Short triumphant jingle for finding treasure.
- **Use when:** Discovering a significant treasure.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.46s
- **Sonic profile:** Medium (1.46s), mid, bass-present; voices: pulse wave, triangle wave; echoing tail.
- **Tags:** items, treasure, found, pure
- **File:** `sfx/02-items/treasure-found.sb`

## Movement (`03-movement`)

Jumping, landing, footsteps and other movement.

### `03-movement/dash` — Dash

- **Description:** Quick whoosh with a falling hiss.
- **Use when:** Dashing or dodging.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.25s
- **Sonic profile:** Short (0.25s), very dark, light low end; voices: triangle wave, noise; pitch falls, pitch rises, noisy/breathy.
- **Tags:** movement, dash, neutral
- **File:** `sfx/03-movement/dash.sb`

### `03-movement/double-jump` — Double Jump

- **Description:** Second jump in the air, higher and snappier.
- **Use when:** A second jump in mid-air.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.18s
- **Sonic profile:** Short (0.18s), mid, light low end; voices: pulse wave; pitch rises.
- **Tags:** movement, double, jump, neutral
- **File:** `sfx/03-movement/double-jump.sb`

### `03-movement/footstep-grass` — Footstep Grass

- **Description:** One soft footstep on grass.
- **Use when:** A step on soft ground or grass.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.06s
- **Sonic profile:** Tick (0.06s), very dark, bass-heavy; voices: noise; noisy/breathy.
- **Tags:** movement, footstep, grass, neutral
- **File:** `sfx/03-movement/footstep-grass.sb`

### `03-movement/footstep-stone` — Footstep Stone

- **Description:** One footstep on stone.
- **Use when:** A step on stone floor, such as in the Ashen Citadel; vary with random pitch or timing.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.06s
- **Sonic profile:** Tick (0.06s), very dark, bass-heavy; voices: sine, noise; noisy/breathy.
- **Tags:** movement, footstep, stone, neutral
- **File:** `sfx/03-movement/footstep-stone.sb`

### `03-movement/jump` — Jump

- **Description:** Standard jump: a quick upward chirp.
- **Use when:** Standard jump (see 18-corrupted/corrupted-jump for corrupted ground).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.18s
- **Sonic profile:** Short (0.18s), mid, light low end; voices: pulse wave; pitch rises.
- **Tags:** movement, jump, neutral
- **File:** `sfx/03-movement/jump.sb`

### `03-movement/land-thud` — Land Thud

- **Description:** Landing: a soft thud with a click.
- **Use when:** Landing after a jump or fall (see 18-corrupted/corrupted-land).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.14s
- **Sonic profile:** Tick (0.14s), very dark, bass-heavy; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** movement, land, thud, neutral
- **File:** `sfx/03-movement/land-thud.sb`

### `03-movement/slide-skid` — Slide Skid

- **Description:** Skidding along the ground.
- **Use when:** Sliding or skidding along the ground.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), dark, light low end; voices: noise; tremolo pulsing, noisy/breathy.
- **Tags:** movement, slide, skid, neutral
- **File:** `sfx/03-movement/slide-skid.sb`

### `03-movement/spring-bounce` — Spring Bounce

- **Description:** Boing off a spring pad.
- **Use when:** Bouncing on a spring pad; arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), dark, light low end; voices: pulse wave; pitch rises, vibrato.
- **Tags:** movement, spring, bounce, neutral
- **File:** `sfx/03-movement/spring-bounce.sb`

### `03-movement/swim-splash` — Swim Splash

- **Description:** Splash with a few rising bubbles.
- **Use when:** Entering or moving through water, such as the Weeping Marsh.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.26s
- **Sonic profile:** Short (0.26s), dark, bass-present; voices: sine, noise; pitch rises, noisy/breathy.
- **Tags:** movement, swim, splash, neutral
- **File:** `sfx/03-movement/swim-splash.sb`

### `03-movement/wall-scrape` — Wall Scrape

- **Description:** Scrape while sliding down a wall.
- **Use when:** Sliding down a wall.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.25s
- **Sonic profile:** Short (0.25s), dark, light low end; voices: noise; tremolo pulsing, noisy/breathy.
- **Tags:** movement, wall, scrape, neutral
- **File:** `sfx/03-movement/wall-scrape.sb`

### `03-movement/wing-flap` — Wing Flap

- **Description:** Two soft flaps.
- **Use when:** A flying creature or the player gliding flaps.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.22s
- **Sonic profile:** Short (0.22s), very dark, bass-present; voices: noise; pitch falls, noisy/breathy.
- **Tags:** movement, wing, flap, neutral
- **File:** `sfx/03-movement/wing-flap.sb`

## Melee combat (`04-combat`)

Melee hits, blocks and enemy reactions.

### `04-combat/block-break` — Block Break

- **Description:** Breakable block shattering.
- **Use when:** A breakable wall or block is destroyed.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.85s
- **Sonic profile:** Medium (0.85s), bright, light low end; voices: FM bell/e-piano tone, noise; echoing tail, noisy/breathy.
- **Tags:** combat, block, break, neutral
- **File:** `sfx/04-combat/block-break.sb`

### `04-combat/critical-hit` — Critical Hit

- **Description:** Critical strike: zap, heavy hit and a bell ring.
- **Use when:** A critical hit lands.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 1.01s
- **Sonic profile:** Medium (1.01s), very bright, light low end; voices: pulse wave, sine, FM bell/e-piano tone, noise; pitch falls, echoing tail, noisy/breathy.
- **Tags:** combat, critical, hit, neutral
- **File:** `sfx/04-combat/critical-hit.sb`

### `04-combat/enemy-defeat` — Enemy Defeat

- **Description:** Enemy defeated: a descending pop.
- **Use when:** A basic enemy is defeated (see 15-enemies/vanish-into-smoke for spirit enemies).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.28s
- **Sonic profile:** Short (0.28s), bright, light low end; voices: pulse wave, noise; pitch falls, noisy/breathy.
- **Tags:** combat, enemy, defeat, neutral
- **File:** `sfx/04-combat/enemy-defeat.sb`

### `04-combat/enemy-hurt` — Enemy Hurt

- **Description:** Enemy takes damage: a falling yelp.
- **Use when:** An enemy is damaged but not defeated.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.22s
- **Sonic profile:** Short (0.22s), dark, light low end; voices: pulse wave; pitch falls, vibrato.
- **Tags:** combat, enemy, hurt, neutral
- **File:** `sfx/04-combat/enemy-hurt.sb`

### `04-combat/heavy-hit` — Heavy Hit

- **Description:** Heavy blow with a deep sub-bass boom.
- **Use when:** A powerful blow lands (heavy weapon, boss attack).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), very dark, bass-heavy; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** combat, heavy, hit, neutral
- **File:** `sfx/04-combat/heavy-hit.sb`

### `04-combat/parry-clang` — Parry Clang

- **Description:** Metal-on-metal parry.
- **Use when:** The player parries or a block is perfectly timed.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.4s
- **Sonic profile:** Short (0.40s), very bright, light low end; voices: FM bell/e-piano tone, noise; noisy/breathy.
- **Tags:** combat, parry, clang, neutral
- **File:** `sfx/04-combat/parry-clang.sb`

### `04-combat/shield-block` — Shield Block

- **Description:** Blow absorbed by a shield.
- **Use when:** A blow is absorbed by a shield.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.15s
- **Sonic profile:** Short (0.15s), very dark, bass-heavy; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** combat, shield, block, neutral
- **File:** `sfx/04-combat/shield-block.sb`

### `04-combat/stab` — Stab

- **Description:** Quick thrust.
- **Use when:** A quick thrust attack.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), mid, light low end; voices: pulse wave, noise; pitch rises, noisy/breathy.
- **Tags:** combat, stab, neutral
- **File:** `sfx/04-combat/stab.sb`

### `04-combat/sword-hit` — Sword Hit

- **Description:** Blade connecting: crack, ring and thump.
- **Use when:** A melee weapon connects with an enemy.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.12s
- **Sonic profile:** Tick (0.12s), very dark, bass-heavy; voices: pulse wave, sine, noise; pitch falls, noisy/breathy.
- **Tags:** combat, sword, hit, neutral
- **File:** `sfx/04-combat/sword-hit.sb`

### `04-combat/sword-swing` — Sword Swing

- **Description:** Blade whooshing through the air.
- **Use when:** A melee weapon swings and misses.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.16s
- **Sonic profile:** Short (0.16s), mid, light low end; voices: noise; pitch falls, noisy/breathy.
- **Tags:** combat, sword, swing, neutral
- **File:** `sfx/04-combat/sword-swing.sb`

## Magic & ranged (`05-magic`)

General spell and ranged-attack sounds. See 14-spells for realm-specific spells.

### `05-magic/arrow-shot` — Arrow Shot

- **Description:** Bowstring twang and release.
- **Use when:** An arrow or bolt is fired.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.14s
- **Sonic profile:** Tick (0.14s), mid, light low end; voices: pulse wave, noise; pitch rises, noisy/breathy.
- **Tags:** magic, arrow, shot, neutral
- **File:** `sfx/05-magic/arrow-shot.sb`

### `05-magic/charge-release` — Charge Release

- **Description:** The blast: a boom, a noise burst and a zap.
- **Use when:** Releasing a charged attack.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.5s
- **Sonic profile:** Medium (0.50s), very dark, bass-heavy; voices: pulse wave, sine, noise; pitch falls, noisy/breathy.
- **Tags:** magic, charge, release, neutral
- **File:** `sfx/05-magic/charge-release.sb`

### `05-magic/charge-up` — Charge Up

- **Description:** Power building: a long rising sweep.
- **Use when:** Charging a powerful attack or spell.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), very dark, bass-present; voices: pulse wave, noise; pitch rises, sweeping pulse width, noisy/breathy.
- **Tags:** magic, charge, up, corrupted
- **File:** `sfx/05-magic/charge-up.sb`

### `05-magic/dark-curse` — Dark Curse

- **Description:** Wobbling low drone with a tritone growl.
- **Use when:** Casting a curse or dark spell.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.85s
- **Sonic profile:** Medium (0.85s), very dark, bass-present; voices: sawtooth, FM bell/e-piano tone; vibrato, tremolo pulsing.
- **Tags:** magic, dark, curse, corrupted
- **File:** `sfx/05-magic/dark-curse.sb`

### `05-magic/fireball-cast` — Fireball Cast

- **Description:** Fire gathering and launching.
- **Use when:** Casting a fire spell.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.4s
- **Sonic profile:** Short (0.40s), very dark, bass-heavy; voices: sawtooth, noise; pitch rises, noisy/breathy.
- **Tags:** magic, fireball, cast, neutral
- **File:** `sfx/05-magic/fireball-cast.sb`

### `05-magic/heal-spell` — Heal Spell

- **Description:** Rising bells over a warm organ swell.
- **Use when:** Casting a healing spell (pure palette).
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), very bright, light low end; voices: FM bell/e-piano tone, organ; echoing tail.
- **Tags:** magic, heal, spell, pure
- **File:** `sfx/05-magic/heal-spell.sb`

### `05-magic/ice-shard` — Ice Shard

- **Description:** Icy FM ring with a scatter of hat ticks.
- **Use when:** Casting or hitting with an ice spell.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.8s
- **Sonic profile:** Medium (0.80s), bright, light low end; voices: FM bell/e-piano tone, noise; echoing tail, noisy/breathy.
- **Tags:** magic, ice, shard, neutral
- **File:** `sfx/05-magic/ice-shard.sb`

### `05-magic/laser-shot` — Laser Shot

- **Description:** Pew: a fast falling sweep.
- **Use when:** A beam weapon fires; sci-fi flavour, does not suit this setting.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.16s
- **Sonic profile:** Short (0.16s), bright, light low end; voices: pulse wave; pitch falls.
- **Tags:** magic, laser, shot, neutral
- **File:** `sfx/05-magic/laser-shot.sb`

### `05-magic/lightning` — Lightning

- **Description:** Crackling burst with a falling zigzag.
- **Use when:** Casting a lightning spell or a lightning strike.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.28s
- **Sonic profile:** Short (0.28s), bright, light low end; voices: pulse wave, noise; tremolo pulsing, noisy/breathy.
- **Tags:** magic, lightning, neutral
- **File:** `sfx/05-magic/lightning.sb`

### `05-magic/plasma-bolt` — Plasma Bolt

- **Description:** Chunky saw bolt with a throbbing tail.
- **Use when:** A plasma shot fires; sci-fi flavour, does not suit this setting.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.82s
- **Sonic profile:** Medium (0.82s), dark, light low end; voices: sawtooth; pitch falls, tremolo pulsing, detuned/chorused, echoing tail.
- **Tags:** magic, plasma, bolt, neutral
- **File:** `sfx/05-magic/plasma-bolt.sb`

### `05-magic/poison-bubble` — Poison Bubble

- **Description:** Gloopy bubbling.
- **Use when:** A poison or acid effect bubbles.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.35s
- **Sonic profile:** Short (0.35s), very dark, light low end; voices: sine; pitch rises, vibrato.
- **Tags:** magic, poison, bubble, corrupted
- **File:** `sfx/05-magic/poison-bubble.sb`

### `05-magic/shield-up` — Shield Up

- **Description:** Protective barrier swelling into place.
- **Use when:** Raising a magic shield (see 14-spells/ward-barrier).
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 0.6s
- **Sonic profile:** Medium (0.60s), mid, light low end; voices: pulse wave, FM bell/e-piano tone; pitch rises, vibrato.
- **Tags:** magic, shield, up, pure
- **File:** `sfx/05-magic/shield-up.sb`

### `05-magic/summon` — Summon

- **Description:** Dark swell, noise rise, then a bell call.
- **Use when:** Summoning an ally or creature.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.9s
- **Sonic profile:** Long (1.90s), bright, bass-present; voices: FM bell/e-piano tone, organ, noise; pitch rises, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** magic, summon, corrupted
- **File:** `sfx/05-magic/summon.sb`

### `05-magic/teleport` — Teleport

- **Description:** Phasing sweep with a pop at the end.
- **Use when:** Teleporting a long distance (see 14-spells/shadow-step for short blinks).
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.46s
- **Sonic profile:** Short (0.46s), mid, light low end; voices: pulse wave, sine; pitch rises, sweeping pulse width.
- **Tags:** magic, teleport, neutral
- **File:** `sfx/05-magic/teleport.sb`

### `05-magic/wind-gust` — Wind Gust

- **Description:** A gust of wind that swells and fades.
- **Use when:** A wind spell or a strong gust.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), very dark, bass-present; voices: noise; pitch rises, tremolo pulsing, noisy/breathy.
- **Tags:** magic, wind, gust, neutral
- **File:** `sfx/05-magic/wind-gust.sb`

## Explosions & impacts (`06-explosions`)

Blasts, crashes and big impacts.

### `06-explosions/bomb-fuse` — Bomb Fuse

- **Description:** Hissing, sputtering fuse.
- **Use when:** A fuse burns; arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.6s
- **Sonic profile:** Medium (0.60s), dark, light low end; voices: noise; tremolo pulsing, noisy/breathy.
- **Tags:** explosions, bomb, fuse, neutral
- **File:** `sfx/06-explosions/bomb-fuse.sb`

### `06-explosions/cannon-fire` — Cannon Fire

- **Description:** Cannon: boom with a long low tail.
- **Use when:** A cannon fires; does not suit a spirit realm.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.55s
- **Sonic profile:** Medium (0.55s), very dark, bass-heavy; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** explosions, cannon, fire, neutral
- **File:** `sfx/06-explosions/cannon-fire.sb`

### `06-explosions/explosion-large` — Explosion Large

- **Description:** Big blast with a long sub-bass tail.
- **Use when:** A large explosion or major destruction.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), very dark, bass-heavy; voices: sine, noise; pitch falls, pitch rises, echoing tail, noisy/breathy.
- **Tags:** explosions, explosion, large, neutral
- **File:** `sfx/06-explosions/explosion-large.sb`

### `06-explosions/explosion-small` — Explosion Small

- **Description:** Small blast: noise burst over a quick boom.
- **Use when:** A small explosion or blast.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.38s
- **Sonic profile:** Short (0.38s), very dark, bass-heavy; voices: sine, noise; pitch falls, pitch rises, noisy/breathy.
- **Tags:** explosions, explosion, small, neutral
- **File:** `sfx/06-explosions/explosion-small.sb`

### `06-explosions/glass-shatter` — Glass Shatter

- **Description:** Breaking glass.
- **Use when:** Glass or crystal shatters.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.82s
- **Sonic profile:** Medium (0.82s), very bright, light low end; voices: FM bell/e-piano tone, noise; echoing tail, noisy/breathy.
- **Tags:** explosions, glass, shatter, neutral
- **File:** `sfx/06-explosions/glass-shatter.sb`

### `06-explosions/gun-shot` — Gun Shot

- **Description:** Retro gunshot: crack with a falling zap.
- **Use when:** A gunshot; does not suit a spirit realm.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.12s
- **Sonic profile:** Tick (0.12s), very dark, bass-present; voices: pulse wave, noise; pitch falls, noisy/breathy.
- **Tags:** explosions, gun, shot, neutral
- **File:** `sfx/06-explosions/gun-shot.sb`

### `06-explosions/impact-slam` — Impact Slam

- **Description:** Heavy slam: a deep thump and a tick.
- **Use when:** A heavy slam, ground pound or boss stomp.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.38s
- **Sonic profile:** Short (0.38s), very dark, bass-heavy; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** explosions, impact, slam, neutral
- **File:** `sfx/06-explosions/impact-slam.sb`

### `06-explosions/metal-crash` — Metal Crash

- **Description:** Metallic crash.
- **Use when:** Metal collapses or a heavy object crashes.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.7s
- **Sonic profile:** Medium (0.70s), very bright, light low end; voices: FM bell/e-piano tone, noise; noisy/breathy.
- **Tags:** explosions, metal, crash, neutral
- **File:** `sfx/06-explosions/metal-crash.sb`

### `06-explosions/rock-fall` — Rock Fall

- **Description:** Tumbling rocks.
- **Use when:** Rocks tumble or a cave-in begins.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.61s
- **Sonic profile:** Medium (0.61s), very dark, bass-heavy; voices: noise; noisy/breathy.
- **Tags:** explosions, rock, fall, neutral
- **File:** `sfx/06-explosions/rock-fall.sb`

### `06-explosions/rumble` — Rumble

- **Description:** Low rumbling, like a collapsing tunnel.
- **Use when:** A collapsing tunnel, earthquake or tension rumble.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), very dark, bass-heavy; voices: sine, noise; tremolo pulsing, noisy/breathy.
- **Tags:** explosions, rumble, corrupted
- **File:** `sfx/06-explosions/rumble.sb`

### `06-explosions/thunder` — Thunder

- **Description:** A sharp crack followed by a long rolling rumble.
- **Use when:** A thunderclap or storm.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.78s
- **Sonic profile:** Long (1.78s), very dark, bass-heavy; voices: noise; vibrato, noisy/breathy.
- **Tags:** explosions, thunder, neutral
- **File:** `sfx/06-explosions/thunder.sb`

## Damage & death (`07-damage`)

Player damage, death and defeat sounds.

### `07-damage/boss-defeat` — Boss Defeat

- **Description:** Boss falls: a cascade of blasts and a long fall.
- **Use when:** A boss is defeated (see 15-enemies/boss-collapse for the realm version).
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 2.5s
- **Sonic profile:** Long (2.50s), mid, bass-heavy; voices: pulse wave, sine, noise; pitch falls, echoing tail, noisy/breathy.
- **Tags:** damage, boss, defeat, neutral
- **File:** `sfx/07-damage/boss-defeat.sb`

### `07-damage/freeze` — Freeze

- **Description:** Frozen solid: a glassy ring and hiss.
- **Use when:** The player or an enemy is frozen.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), very bright, light low end; voices: FM bell/e-piano tone, noise; echoing tail, noisy/breathy.
- **Tags:** damage, freeze, corrupted
- **File:** `sfx/07-damage/freeze.sb`

### `07-damage/game-over` — Game Over

- **Description:** Descending minor game-over jingle.
- **Use when:** The game-over screen.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 2.2s
- **Sonic profile:** Long (2.20s), dark, bass-present; voices: pulse wave, triangle wave; vibrato, echoing tail.
- **Tags:** damage, game, over, corrupted
- **File:** `sfx/07-damage/game-over.sb`

### `07-damage/low-health-beep` — Low Health Beep

- **Description:** Repeating warning beep for low health.
- **Use when:** Repeating warning when health is low.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.6s
- **Sonic profile:** Medium (0.60s), mid, light low end; voices: pulse wave.
- **Tags:** damage, low, health, beep, neutral
- **File:** `sfx/07-damage/low-health-beep.sb`

### `07-damage/player-death` — Player Death

- **Description:** Long falling cry with a thud.
- **Use when:** The player dies.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.1s
- **Sonic profile:** Medium (1.10s), very dark, bass-heavy; voices: pulse wave, sine, noise; pitch falls, vibrato, noisy/breathy.
- **Tags:** damage, player, death, corrupted
- **File:** `sfx/07-damage/player-death.sb`

### `07-damage/player-hurt` — Player Hurt

- **Description:** You take a hit: a falling cry with a click.
- **Use when:** The player takes damage.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.24s
- **Sonic profile:** Short (0.24s), mid, light low end; voices: pulse wave, noise; pitch falls, vibrato, noisy/breathy.
- **Tags:** damage, player, hurt, neutral
- **File:** `sfx/07-damage/player-hurt.sb`

### `07-damage/poison-tick` — Poison Tick

- **Description:** One tick of poison damage.
- **Use when:** One damage tick of poison.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), very dark, light low end; voices: triangle wave; pitch rises.
- **Tags:** damage, poison, tick, corrupted
- **File:** `sfx/07-damage/poison-tick.sb`

### `07-damage/revive` — Revive

- **Description:** Back on your feet: bells rising over a swell.
- **Use when:** The player is revived.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), bright, light low end; voices: FM bell/e-piano tone, organ; echoing tail.
- **Tags:** damage, revive, pure
- **File:** `sfx/07-damage/revive.sb`

### `07-damage/shield-break` — Shield Break

- **Description:** Shield shattering with a low crack.
- **Use when:** A shield or ward is destroyed.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.85s
- **Sonic profile:** Medium (0.85s), bright, light low end; voices: sine, FM bell/e-piano tone, noise; pitch falls, echoing tail, noisy/breathy.
- **Tags:** damage, shield, break, neutral
- **File:** `sfx/07-damage/shield-break.sb`

### `07-damage/stun` — Stun

- **Description:** Dizzy wobble.
- **Use when:** The player or an enemy is stunned.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.55s
- **Sonic profile:** Medium (0.55s), mid, light low end; voices: pulse wave; pitch falls, vibrato, sweeping pulse width.
- **Tags:** damage, stun, corrupted
- **File:** `sfx/07-damage/stun.sb`

## Environment (`08-environment`)

Short environmental one-shots. For long ambience see 17-zones.

### `08-environment/door-creak` — Door Creak

- **Description:** Slow creaking door.
- **Use when:** Opening an old door slowly.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.55s
- **Sonic profile:** Medium (0.55s), very dark, bass-present; voices: sawtooth, noise; pitch rises, vibrato, tremolo pulsing, noisy/breathy.
- **Tags:** environment, door, creak, corrupted
- **File:** `sfx/08-environment/door-creak.sb`

### `08-environment/door-slam` — Door Slam

- **Description:** Door slamming shut.
- **Use when:** A door slams shut.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.2s
- **Sonic profile:** Short (0.20s), very dark, bass-heavy; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** environment, door, slam, neutral
- **File:** `sfx/08-environment/door-slam.sb`

### `08-environment/eerie-drone` — Eerie Drone

- **Description:** Cold, unsettling drone.
- **Use when:** Unsettling short drone for a creepy moment.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), very dark, bass-present; voices: FM bell/e-piano tone, organ; vibrato, tremolo pulsing.
- **Tags:** environment, eerie, drone, corrupted
- **File:** `sfx/08-environment/eerie-drone.sb`

### `08-environment/fire-crackle` — Fire Crackle

- **Description:** Crackling fire over a low rumble.
- **Use when:** A campfire or torch crackles.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.55s
- **Sonic profile:** Medium (0.55s), very dark, bass-heavy; voices: noise; tremolo pulsing, noisy/breathy.
- **Tags:** environment, fire, crackle, neutral
- **File:** `sfx/08-environment/fire-crackle.sb`

### `08-environment/gate-open` — Gate Open

- **Description:** Heavy gate grinding open.
- **Use when:** A heavy gate or portcullis opens.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.1s
- **Sonic profile:** Medium (1.10s), very dark, bass-heavy; voices: sawtooth, noise; pitch rises, vibrato, tremolo pulsing, noisy/breathy.
- **Tags:** environment, gate, open, neutral
- **File:** `sfx/08-environment/gate-open.sb`

### `08-environment/heartbeat` — Heartbeat

- **Description:** Slow, tense heartbeat (two beats).
- **Use when:** Tension: two slow heartbeats.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.78s
- **Sonic profile:** Long (1.78s), very dark, bass-heavy; voices: sine; pitch falls.
- **Tags:** environment, heartbeat, corrupted
- **File:** `sfx/08-environment/heartbeat.sb`

### `08-environment/lever-pull` — Lever Pull

- **Description:** Ratcheting lever with a heavy clunk.
- **Use when:** Pulling a lever.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.37s
- **Sonic profile:** Short (0.37s), very dark, bass-heavy; voices: sine, noise; noisy/breathy.
- **Tags:** environment, lever, pull, neutral
- **File:** `sfx/08-environment/lever-pull.sb`

### `08-environment/machine-hum` — Machine Hum

- **Description:** Low industrial hum.
- **Use when:** An industrial machine hums; sci-fi flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), very dark, bass-heavy; voices: sawtooth; tremolo pulsing, detuned/chorused.
- **Tags:** environment, machine, hum, neutral
- **File:** `sfx/08-environment/machine-hum.sb`

### `08-environment/portal-hum` — Portal Hum

- **Description:** Swirling portal energy.
- **Use when:** A portal or magical device idles nearby (short; see 17-zones for long loops).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), very dark, bass-heavy; voices: sawtooth, FM bell/e-piano tone; vibrato, tremolo pulsing, detuned/chorused.
- **Tags:** environment, portal, hum, corrupted
- **File:** `sfx/08-environment/portal-hum.sb`

### `08-environment/switch-click` — Switch Click

- **Description:** Click of a small switch.
- **Use when:** Flipping a switch or pressing a button.
- **Palette:** neutral · **Zone:** any · **Theme fit:** usable · **Duration:** 0.08s
- **Sonic profile:** Tick (0.08s), mid, light low end; voices: pulse wave, noise; noisy/breathy.
- **Tags:** environment, switch, click, neutral
- **File:** `sfx/08-environment/switch-click.sb`

### `08-environment/water-drip` — Water Drip

- **Description:** Single echoing drip.
- **Use when:** A single echoing drip; ambient one-shot for caves and marsh.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.62s
- **Sonic profile:** Medium (0.62s), mid, light low end; voices: sine; pitch falls, echoing tail.
- **Tags:** environment, water, drip, neutral
- **File:** `sfx/08-environment/water-drip.sb`

### `08-environment/wind-howl` — Wind Howl

- **Description:** Eerie wind with a slow wobble.
- **Use when:** A cold wind sweeps through; ambience for exposed areas.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), dark, bass-present; voices: noise; pitch rises, tremolo pulsing, noisy/breathy.
- **Tags:** environment, wind, howl, corrupted
- **File:** `sfx/08-environment/wind-howl.sb`

## Battle events (`09-battle`)

Battle start, boss and warning sounds.

### `09-battle/alarm` — Alarm

- **Description:** Two-tone alarm, three times.
- **Use when:** An alarm sounds; modern/arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 1.58s
- **Sonic profile:** Long (1.58s), mid, light low end; voices: pulse wave; echoing tail.
- **Tags:** battle, alarm, neutral
- **File:** `sfx/09-battle/alarm.sb`

### `09-battle/battle-start` — Battle Start

- **Description:** Encounter sting: a boom, a rising chirp and a minor stab.
- **Use when:** A battle or encounter begins.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.92s
- **Sonic profile:** Medium (0.92s), very dark, bass-heavy; voices: pulse wave, sawtooth, sine, noise; pitch falls, pitch rises, detuned/chorused, noisy/breathy.
- **Tags:** battle, start, corrupted
- **File:** `sfx/09-battle/battle-start.sb`

### `09-battle/boss-roar` — Boss Roar

- **Description:** Huge growl: a low saw glide over rumbling noise.
- **Use when:** A boss roars or announces itself.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.1s
- **Sonic profile:** Medium (1.10s), very dark, bass-heavy; voices: sawtooth, noise; pitch falls, vibrato, tremolo pulsing, detuned/chorused, noisy/breathy.
- **Tags:** battle, boss, roar, corrupted
- **File:** `sfx/09-battle/boss-roar.sb`

### `09-battle/combo-ladder` — Combo Ladder

- **Description:** Rising combo hits.
- **Use when:** Chained hits build a combo; arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 1.05s
- **Sonic profile:** Medium (1.05s), bright, light low end; voices: pulse wave; echoing tail.
- **Tags:** battle, combo, ladder, neutral
- **File:** `sfx/09-battle/combo-ladder.sb`

### `09-battle/countdown` — Countdown

- **Description:** Three short beeps, then a long one.
- **Use when:** A three-beep countdown; arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 2.1s
- **Sonic profile:** Long (2.10s), mid, light low end; voices: pulse wave.
- **Tags:** battle, countdown, neutral
- **File:** `sfx/09-battle/countdown.sb`

### `09-battle/enemy-spotted` — Enemy Spotted

- **Description:** Alert: you've been seen.
- **Use when:** An enemy notices the player.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.86s
- **Sonic profile:** Medium (0.86s), very bright, light low end; voices: pulse wave, FM bell/e-piano tone; pitch rises, echoing tail.
- **Tags:** battle, enemy, spotted, neutral
- **File:** `sfx/09-battle/enemy-spotted.sb`

### `09-battle/low-health-heartbeat` — Low Health Heartbeat

- **Description:** Fast, urgent heartbeat for critical health.
- **Use when:** Urgent heartbeat when health is critical.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), very dark, bass-heavy; voices: sine; pitch falls.
- **Tags:** battle, low, health, heartbeat, corrupted
- **File:** `sfx/09-battle/low-health-heartbeat.sb`

### `09-battle/phase-change` — Phase Change

- **Description:** Boss changes phase: rumble, riser and a hit.
- **Use when:** A boss enters a new phase (see 15-enemies/boss-surge).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), very dark, bass-heavy; voices: pulse wave, sine, noise; pitch falls, pitch rises, noisy/breathy.
- **Tags:** battle, phase, change, corrupted
- **File:** `sfx/09-battle/phase-change.sb`

### `09-battle/round-start` — Round Start

- **Description:** 'Fight!': a punchy brass-like fanfare.
- **Use when:** A fight round starts; arcade/fighting-game flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.91s
- **Sonic profile:** Medium (0.91s), very dark, bass-present; voices: triangle wave, sawtooth; detuned/chorused.
- **Tags:** battle, round, start, neutral
- **File:** `sfx/09-battle/round-start.sb`

### `09-battle/timer-tick` — Timer Tick

- **Description:** Clock tick (four ticks, speeding up).
- **Use when:** A ticking timer; arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 0.84s
- **Sonic profile:** Medium (0.84s), mid, light low end; voices: pulse wave.
- **Tags:** battle, timer, tick, neutral
- **File:** `sfx/09-battle/timer-tick.sb`

## Jingles & stingers (`10-jingles`)

Short musical rewards and stings, in F minor.

### `10-jingles/achievement` — Achievement

- **Description:** Bell triad climbing to a high ring.
- **Use when:** An achievement unlocks.
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 1.7s
- **Sonic profile:** Long (1.70s), very bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** jingles, achievement, pure
- **File:** `sfx/10-jingles/achievement.sb`

### `10-jingles/checkpoint` — Checkpoint

- **Description:** Two soft bells and an organ glow.
- **Use when:** Reaching a checkpoint.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), mid, light low end; voices: FM bell/e-piano tone, organ; echoing tail.
- **Tags:** jingles, checkpoint, pure
- **File:** `sfx/10-jingles/checkpoint.sb`

### `10-jingles/defeat-sting` — Defeat Sting

- **Description:** Falling minor sting.
- **Use when:** Losing a battle or failing a task.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 2.4s
- **Sonic profile:** Long (2.40s), dark, light low end; voices: pulse wave, sawtooth; vibrato, detuned/chorused, echoing tail.
- **Tags:** jingles, defeat, sting, corrupted
- **File:** `sfx/10-jingles/defeat-sting.sb`

### `10-jingles/level-complete` — Level Complete

- **Description:** Rising F arpeggio with a bright major landing.
- **Use when:** Completing a level or area.
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 2.0s
- **Sonic profile:** Long (2.00s), mid, bass-present; voices: pulse wave, triangle wave; echoing tail.
- **Tags:** jingles, level, complete, pure
- **File:** `sfx/10-jingles/level-complete.sb`

### `10-jingles/level-up` — Level Up

- **Description:** Rising scale with a sparkling top note.
- **Use when:** The player levels up (see 18-corrupted/corrupted-level-up).
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), mid, light low end; voices: pulse wave, FM bell/e-piano tone; echoing tail.
- **Tags:** jingles, level, up, pure
- **File:** `sfx/10-jingles/level-up.sb`

### `10-jingles/new-high-score` — New High Score

- **Description:** Ascending run with a bouncing trill.
- **Use when:** A new high score; arcade flavour.
- **Palette:** neutral · **Zone:** any · **Theme fit:** off-theme · **Duration:** 1.66s
- **Sonic profile:** Long (1.66s), bright, light low end; voices: pulse wave; echoing tail.
- **Tags:** jingles, new, high, score, neutral
- **File:** `sfx/10-jingles/new-high-score.sb`

### `10-jingles/quest-complete` — Quest Complete

- **Description:** Slow, regal resolution.
- **Use when:** Completing a quest.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 2.15s
- **Sonic profile:** Long (2.15s), mid, light low end; voices: pulse wave, FM bell/e-piano tone, organ; vibrato, echoing tail.
- **Tags:** jingles, quest, complete, pure
- **File:** `sfx/10-jingles/quest-complete.sb`

### `10-jingles/secret-found` — Secret Found

- **Description:** Chromatic sparkle for a discovery.
- **Use when:** Discovering a secret.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.42s
- **Sonic profile:** Medium (1.42s), very bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** jingles, secret, found, pure
- **File:** `sfx/10-jingles/secret-found.sb`

### `10-jingles/title-sting` — Title Sting

- **Description:** Dark organ chord for a title screen.
- **Use when:** The title screen appears.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 2.5s
- **Sonic profile:** Long (2.50s), mid, bass-present; voices: FM bell/e-piano tone, organ; tremolo pulsing, echoing tail.
- **Tags:** jingles, title, sting, corrupted
- **File:** `sfx/10-jingles/title-sting.sb`

### `10-jingles/victory-fanfare` — Victory Fanfare

- **Description:** Triumphant fanfare: rising fourths into a held high note.
- **Use when:** Winning a battle or finishing a major task.
- **Palette:** pure · **Zone:** any · **Theme fit:** usable · **Duration:** 3.0s
- **Sonic profile:** Long (3.00s), mid, bass-present; voices: pulse wave, triangle wave; vibrato, echoing tail.
- **Tags:** jingles, victory, fanfare, pure
- **File:** `sfx/10-jingles/victory-fanfare.sb`

## Spirit & soul (`11-spirit`)

Soul, spirit-form, possession, purification and corruption mechanics.

### `11-spirit/banish` — Banish

- **Description:** A spirit is cast out: a falling sweep scatters into noise, ending on a low thud.
- **Use when:** The player banishes or exorcises a lesser spirit, or an enemy spirit is dispelled.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 0.7s
- **Sonic profile:** Medium (0.70s), dark, bass-heavy; voices: pulse wave, sine, noise; pitch falls, noisy/breathy.
- **Tags:** spirit, banish, pure, dispel, cast out, exorcise
- **File:** `sfx/11-spirit/banish.sb`

### `11-spirit/corruption-spread` — Corruption Spread

- **Description:** Corruption creeping outward: pulsing noise and a swelling detuned drone with a sour wobble.
- **Use when:** Corruption spreads onto a new area, tile or character, or a corruption event begins.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), very dark, bass-heavy; voices: FM bell/e-piano tone, noise; pitch rises, vibrato, tremolo pulsing, detuned/chorused, noisy/breathy.
- **Tags:** spirit, corruption, spread, corrupted, creeping, blight, event
- **File:** `sfx/11-spirit/corruption-spread.sb`

### `11-spirit/corruption-tick` — Corruption Tick

- **Description:** A wet, low squelch: a short crushed thump with a noisy slap.
- **Use when:** Each damage-over-time tick while the player stands in corruption or is corrupted.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), very dark, bass-heavy; voices: sine, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** spirit, corruption, tick, corrupted, damage over time, squelch
- **File:** `sfx/11-spirit/corruption-tick.sb`

### `11-spirit/possession-end` — Possession End

- **Description:** The hold snaps: a noise crack and a falling detuned tone, then silence.
- **Use when:** A possession, charm or mind-control effect ends or is broken.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.95s
- **Sonic profile:** Medium (0.95s), mid, light low end; voices: FM bell/e-piano tone, noise; pitch falls, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** spirit, possession, end, corrupted, break, release, snap
- **File:** `sfx/11-spirit/possession-end.sb`

### `11-spirit/possession-start` — Possession Start

- **Description:** A hostile presence takes hold: an inharmonic FM growl swells under a tremoloing breath and a dissonant tritone stab.
- **Use when:** The player or an NPC is possessed, controlled or overtaken by a spirit.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), very dark, bass-heavy; voices: sawtooth, FM bell/e-piano tone, noise; vibrato, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** spirit, possession, start, corrupted, control, takeover, dread
- **File:** `sfx/11-spirit/possession-start.sb`

### `11-spirit/purify-cleanse` — Purify Cleanse

- **Description:** Corruption washed away: bright bells climb over a swelling organ and resolve to a clean major third.
- **Use when:** The player purifies a corrupted object, area or character; corruption meter drops.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), mid, light low end; voices: FM bell/e-piano tone, organ, noise; pitch rises, echoing tail, noisy/breathy.
- **Tags:** spirit, purify, cleanse, pure, heal corruption, restore
- **File:** `sfx/11-spirit/purify-cleanse.sb`

### `11-spirit/soul-absorb` — Soul Absorb

- **Description:** A wisp of soul drawn into the player: clean bells rise over a warm organ swell with a short airy inhale.
- **Use when:** A soul, spirit essence or ally's spark is collected or absorbed by the player.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.45s
- **Sonic profile:** Medium (1.45s), mid, light low end; voices: FM bell/e-piano tone, organ, noise; pitch rises, echoing tail, noisy/breathy.
- **Tags:** spirit, soul, absorb, pure, collect, gain
- **File:** `sfx/11-spirit/soul-absorb.sb`

### `11-spirit/soul-bind` — Soul Bind

- **Description:** Spectral chains lock: metallic FM clinks close into a held organ chord.
- **Use when:** A soul is bound to an object, a pact is sealed, or an enemy is shackled.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), dark, light low end; voices: FM bell/e-piano tone, organ.
- **Tags:** spirit, soul, bind, neutral, chain, pact, lock, seal
- **File:** `sfx/11-spirit/soul-bind.sb`

### `11-spirit/soul-release` — Soul Release

- **Description:** A soul let go: clean bells descend while a soft exhale of noise rises away.
- **Use when:** A soul is freed, a spirit is laid to rest, or the player lets go of a held soul.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.46s
- **Sonic profile:** Medium (1.46s), mid, light low end; voices: FM bell/e-piano tone, noise; pitch falls, echoing tail, noisy/breathy.
- **Tags:** spirit, soul, release, pure, free, rest
- **File:** `sfx/11-spirit/soul-release.sb`

### `11-spirit/spirit-form-off` — Spirit Form Off

- **Description:** Leaving spirit form: the shimmer falls away and thuds back into a solid body.
- **Use when:** The player returns from spirit form to physical form.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 0.97s
- **Sonic profile:** Medium (0.97s), very dark, bass-heavy; voices: pulse wave, sine; pitch falls, sweeping pulse width, echoing tail.
- **Tags:** spirit, form, off, pure, spirit form, toggle, return, solid
- **File:** `sfx/11-spirit/spirit-form-off.sb`

### `11-spirit/spirit-form-on` — Spirit Form On

- **Description:** Entering spirit form: a shimmering pulse-width sweep rises into a soft glassy bell.
- **Use when:** The player switches into spirit form (to cross the veil, pass through barriers or see hidden things).
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.2s
- **Sonic profile:** Medium (1.20s), mid, light low end; voices: pulse wave, FM bell/e-piano tone; pitch rises, sweeping pulse width, echoing tail.
- **Tags:** spirit, form, on, pure, spirit form, toggle, transform, ethereal
- **File:** `sfx/11-spirit/spirit-form-on.sb`

### `11-spirit/spirit-sight-off` — Spirit Sight Off

- **Description:** The veil closes: the shimmer sinks and fades.
- **Use when:** The player deactivates spirit sight.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), bright, light low end; voices: pulse wave, FM bell/e-piano tone; pitch falls, sweeping pulse width, echoing tail.
- **Tags:** spirit, sight, off, pure, spirit sight, vision, toggle
- **File:** `sfx/11-spirit/spirit-sight-off.sb`

### `11-spirit/spirit-sight-on` — Spirit Sight On

- **Description:** The veil thins: a high shimmering FM pad with a rising glassy sweep.
- **Use when:** The player activates spirit sight to reveal hidden spirits, paths or lore.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), bright, light low end; voices: pulse wave, FM bell/e-piano tone; pitch rises, vibrato, sweeping pulse width, echoing tail.
- **Tags:** spirit, sight, on, pure, spirit sight, vision, reveal, toggle
- **File:** `sfx/11-spirit/spirit-sight-on.sb`

### `11-spirit/whisper-1` — Whisper 1

- **Description:** Breathy spectral whisper #1: pitched noise with a slow wavering pulse, like unintelligible speech just out of earshot.
- **Use when:** Ambient flavour, a haunted object, an NPC the player can't quite hear, or the realm 'speaking' near corruption. Pick randomly among whisper-1..3.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), dark, light low end; voices: noise; pitch rises, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** spirit, whisper, corrupted, voices, ambience, variant, haunted
- **File:** `sfx/11-spirit/whisper-1.sb`

### `11-spirit/whisper-2` — Whisper 2

- **Description:** Breathy spectral whisper #2: pitched noise with a slow wavering pulse, like unintelligible speech just out of earshot.
- **Use when:** Ambient flavour, a haunted object, an NPC the player can't quite hear, or the realm 'speaking' near corruption. Pick randomly among whisper-1..3.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.8s
- **Sonic profile:** Long (1.80s), dark, bass-present; voices: noise; pitch falls, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** spirit, whisper, corrupted, voices, ambience, variant, haunted
- **File:** `sfx/11-spirit/whisper-2.sb`

### `11-spirit/whisper-3` — Whisper 3

- **Description:** Breathy spectral whisper #3: pitched noise with a slow wavering pulse, like unintelligible speech just out of earshot.
- **Use when:** Ambient flavour, a haunted object, an NPC the player can't quite hear, or the realm 'speaking' near corruption. Pick randomly among whisper-1..3.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), dark, bass-present; voices: noise; pitch rises, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** spirit, whisper, corrupted, voices, ambience, variant, haunted
- **File:** `sfx/11-spirit/whisper-3.sb`

## RPG interface (`12-rpg-ui`)

Inventory, equipment, quests, maps, skills and dialogue.

### `12-rpg-ui/dialogue-open` — Dialogue Open

- **Description:** A breath before speech: a low airy swell.
- **Use when:** A conversation or dialogue box opens.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), very dark, bass-heavy; voices: organ, noise; noisy/breathy.
- **Tags:** rpg-ui, dialogue, open, neutral, conversation
- **File:** `sfx/12-rpg-ui/dialogue-open.sb`

### `12-rpg-ui/fast-travel` — Fast Travel

- **Description:** A swirl through the veil: a falling pulse-width sweep over rushing noise and a shimmer.
- **Use when:** Fast-travelling between shrines or zones.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.35s
- **Sonic profile:** Medium (1.35s), mid, light low end; voices: pulse wave, FM bell/e-piano tone, noise; pitch rises, sweeping pulse width, echoing tail, noisy/breathy.
- **Tags:** rpg-ui, fast, travel, neutral, fast travel, teleport, warp, transition
- **File:** `sfx/12-rpg-ui/fast-travel.sb`

### `12-rpg-ui/inventory-close` — Inventory Close

- **Description:** Satchel closing: the open sound reversed, a quick downward swish.
- **Use when:** Closing the inventory or bag.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.16s
- **Sonic profile:** Short (0.16s), dark, light low end; voices: organ, noise; pitch falls, pitch rises, noisy/breathy.
- **Tags:** rpg-ui, inventory, close, neutral, bag, menu
- **File:** `sfx/12-rpg-ui/inventory-close.sb`

### `12-rpg-ui/inventory-open` — Inventory Open

- **Description:** Satchel opening: a soft low organ swell with a short paper-and-cloth swish.
- **Use when:** Opening the inventory or bag.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.2s
- **Sonic profile:** Short (0.20s), dark, light low end; voices: organ, noise; pitch falls, pitch rises, noisy/breathy.
- **Tags:** rpg-ui, inventory, open, neutral, bag, menu
- **File:** `sfx/12-rpg-ui/inventory-open.sb`

### `12-rpg-ui/item-equip` — Item Equip

- **Description:** Gear going on: a small metallic FM clink over a soft thud.
- **Use when:** Equipping a weapon, armour or trinket.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.12s
- **Sonic profile:** Tick (0.12s), very bright, light low end; voices: sine, FM bell/e-piano tone.
- **Tags:** rpg-ui, item, equip, neutral, gear, armor, weapon
- **File:** `sfx/12-rpg-ui/item-equip.sb`

### `12-rpg-ui/item-unequip` — Item Unequip

- **Description:** Gear coming off: a lighter, lower clink and a small rustle.
- **Use when:** Unequipping an item.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), bright, light low end; voices: FM bell/e-piano tone, noise; noisy/breathy.
- **Tags:** rpg-ui, item, unequip, neutral, gear, remove
- **File:** `sfx/12-rpg-ui/item-unequip.sb`

### `12-rpg-ui/map-open` — Map Open

- **Description:** Unfolding a map: a low swish with a soft organ breath.
- **Use when:** Opening the world map.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), very dark, bass-present; voices: organ, noise; pitch falls, noisy/breathy.
- **Tags:** rpg-ui, map, open, neutral, navigation
- **File:** `sfx/12-rpg-ui/map-open.sb`

### `12-rpg-ui/potion-use` — Potion Use

- **Description:** Drinking a potion: four wobbling gulps and a faint bell as it takes effect.
- **Use when:** Using a potion, tonic or consumable.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.12s
- **Sonic profile:** Medium (1.12s), mid, light low end; voices: sine, FM bell/e-piano tone; pitch rises, vibrato, echoing tail.
- **Tags:** rpg-ui, potion, use, neutral, drink, consumable, heal
- **File:** `sfx/12-rpg-ui/potion-use.sb`

### `12-rpg-ui/quest-accept` — Quest Accept

- **Description:** A solemn pact: a low organ stab with a dark bell tolling over it.
- **Use when:** The player accepts a quest.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.2s
- **Sonic profile:** Medium (1.20s), mid, light low end; voices: FM bell/e-piano tone, organ; detuned/chorused, echoing tail.
- **Tags:** rpg-ui, quest, accept, neutral, start, journal
- **File:** `sfx/12-rpg-ui/quest-accept.sb`

### `12-rpg-ui/quest-update` — Quest Update

- **Description:** A single dark bell ping.
- **Use when:** A quest objective updates or a journal entry is added.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), bright, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail.
- **Tags:** rpg-ui, quest, update, neutral, objective, journal
- **File:** `sfx/12-rpg-ui/quest-update.sb`

### `12-rpg-ui/scroll-read` — Scroll Read

- **Description:** Unrolling a scroll: a papery swish followed by a single dark chime.
- **Use when:** Reading a scroll, letter or lore item.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.08s
- **Sonic profile:** Medium (1.08s), bright, light low end; voices: FM bell/e-piano tone, noise; pitch falls, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** rpg-ui, scroll, read, neutral, lore, letter
- **File:** `sfx/12-rpg-ui/scroll-read.sb`

### `12-rpg-ui/skill-unlock` — Skill Unlock

- **Description:** A new power awakens: rising bells and a deep impact underneath.
- **Use when:** The player unlocks a skill, spell or upgrade.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), bright, light low end; voices: sine, FM bell/e-piano tone; pitch falls, echoing tail.
- **Tags:** rpg-ui, skill, unlock, pure, upgrade, power
- **File:** `sfx/12-rpg-ui/skill-unlock.sb`

### `12-rpg-ui/trade-complete` — Trade Complete

- **Description:** Two metallic clinks, the second lower, like soul-coins changing hands.
- **Use when:** A trade or purchase completes at a vendor.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.28s
- **Sonic profile:** Short (0.28s), very bright, light low end; voices: FM bell/e-piano tone.
- **Tags:** rpg-ui, trade, complete, neutral, buy, sell, vendor, currency
- **File:** `sfx/12-rpg-ui/trade-complete.sb`

## Status effects (`13-status`)

Applying, ticking and expiring buffs and debuffs.

### `13-status/bleed-tick` — Bleed Tick

- **Description:** A wet, short pip.
- **Use when:** Each damage tick of a Bleeding status.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.08s
- **Sonic profile:** Tick (0.08s), very dark, light low end; voices: sine, noise; pitch falls, noisy/breathy.
- **Tags:** status, bleed, tick, neutral, damage over time
- **File:** `sfx/13-status/bleed-tick.sb`

### `13-status/blessed-applied` — Blessed Applied

- **Description:** A blessing settles: clean bells in a major triad with a soft shimmer.
- **Use when:** A Blessed or Warded buff is applied.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.2s
- **Sonic profile:** Medium (1.20s), mid, light low end; voices: FM bell/e-piano tone, organ; echoing tail.
- **Tags:** status, blessed, applied, pure, blessing, buff
- **File:** `sfx/13-status/blessed-applied.sb`

### `13-status/corrupted-applied` — Corrupted Applied

- **Description:** Corruption takes the player: a sagging inharmonic tone under a pulsing breath.
- **Use when:** The Corrupted status is applied to the player or a character.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.15s
- **Sonic profile:** Medium (1.15s), very dark, bass-heavy; voices: FM bell/e-piano tone, noise; pitch falls, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** status, corrupted, applied, debuff
- **File:** `sfx/13-status/corrupted-applied.sb`

### `13-status/cursed-applied` — Cursed Applied

- **Description:** A curse lands: a dissonant tritone stab with a trembling low tail.
- **Use when:** The Cursed status is applied.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.1s
- **Sonic profile:** Medium (1.10s), dark, light low end; voices: sawtooth, FM bell/e-piano tone; tremolo pulsing, detuned/chorused, echoing tail.
- **Tags:** status, cursed, applied, corrupted, curse, debuff
- **File:** `sfx/13-status/cursed-applied.sb`

### `13-status/drained-applied` — Drained Applied

- **Description:** Life leaks away: a long falling tone with a soft exhale.
- **Use when:** The Drained or Weakened status is applied.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.8s
- **Sonic profile:** Medium (0.80s), very dark, bass-present; voices: sine, noise; pitch falls, pitch rises, noisy/breathy.
- **Tags:** status, drained, applied, corrupted, drain, weaken, debuff
- **File:** `sfx/13-status/drained-applied.sb`

### `13-status/fear-applied` — Fear Applied

- **Description:** Panic sets in: a rising trembling inharmonic screech over two quick heartbeats.
- **Use when:** The Fear or Terrified status is applied.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.6s
- **Sonic profile:** Medium (0.60s), dark, light low end; voices: sine, FM bell/e-piano tone; pitch falls, pitch rises, vibrato.
- **Tags:** status, fear, applied, corrupted, terror, debuff
- **File:** `sfx/13-status/fear-applied.sb`

### `13-status/rooted-applied` — Rooted Applied

- **Description:** Roots grip the legs: a creaking wooden groan with a slow pulse.
- **Use when:** A Rooted or Immobilized status is applied.
- **Palette:** neutral · **Zone:** hollow-wood · **Theme fit:** core · **Duration:** 0.5s
- **Sonic profile:** Medium (0.50s), very dark, light low end; voices: sawtooth, noise; pitch rises, vibrato, tremolo pulsing, noisy/breathy.
- **Tags:** status, rooted, applied, neutral, root, immobilize
- **File:** `sfx/13-status/rooted-applied.sb`

### `13-status/silenced-applied` — Silenced Applied

- **Description:** A voice stolen: a bell cut short and a muffled noise thud.
- **Use when:** The Silenced status (can't cast spells) is applied.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 0.26s
- **Sonic profile:** Short (0.26s), very dark, bass-heavy; voices: FM bell/e-piano tone, noise; noisy/breathy.
- **Tags:** status, silenced, applied, neutral, silence, mute, debuff
- **File:** `sfx/13-status/silenced-applied.sb`

### `13-status/status-expire` — Status Expire

- **Description:** A soft pair of falling bell notes.
- **Use when:** Any status effect (buff or debuff) wears off.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 0.95s
- **Sonic profile:** Medium (0.95s), mid, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** status, expire, pure, end, wear off
- **File:** `sfx/13-status/status-expire.sb`

## Spells & abilities (`14-spells`)

Spells and abilities for the spirit-realm setting.

### `14-spells/barrier-break` — Barrier Break

- **Description:** A ward shattering: a crack of noise and a falling run of inharmonic bell fragments.
- **Use when:** A barrier, ward or shield is destroyed.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.9s
- **Sonic profile:** Medium (0.90s), very bright, light low end; voices: sine, FM bell/e-piano tone, noise; pitch falls, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** spells, barrier, break, corrupted, spell, shatter
- **File:** `sfx/14-spells/barrier-break.sb`

### `14-spells/exorcism` — Exorcism

- **Description:** A purging burst: layered bells over an organ swell, a sub drop and a rush of noise.
- **Use when:** A powerful holy or exorcism spell that cleanses corruption in an area.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), mid, light low end; voices: sine, FM bell/e-piano tone, organ, noise; pitch falls, echoing tail, noisy/breathy.
- **Tags:** spells, exorcism, pure, spell, holy, purge, area
- **File:** `sfx/14-spells/exorcism.sb`

### `14-spells/ghostfire` — Ghostfire

- **Description:** Cold spectral flame: crackling noise with a shivering high detuned shimmer.
- **Use when:** Casting ghostfire or cold spirit-flame, or standing in it.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.2s
- **Sonic profile:** Medium (1.20s), dark, light low end; voices: FM bell/e-piano tone, noise; vibrato, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** spells, ghostfire, corrupted, spell, fire, flame, cold
- **File:** `sfx/14-spells/ghostfire.sb`

### `14-spells/gravity-well` — Gravity Well

- **Description:** A sucking void: a slow falling sub tone beneath noise that sweeps upward.
- **Use when:** A gravity or pull spell drags enemies in.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), very dark, bass-heavy; voices: sine, noise; pitch rises, vibrato, tremolo pulsing, noisy/breathy.
- **Tags:** spells, gravity, well, corrupted, spell, pull, void, control
- **File:** `sfx/14-spells/gravity-well.sb`

### `14-spells/plague-cloud` — Plague Cloud

- **Description:** A creeping toxic cloud: low gurgling noise over a detuned, wobbling drone.
- **Use when:** A poison, plague or miasma cloud spell.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.0s
- **Sonic profile:** Medium (1.00s), very dark, bass-heavy; voices: FM bell/e-piano tone, noise; pitch rises, vibrato, tremolo pulsing, detuned/chorused, noisy/breathy.
- **Tags:** spells, plague, cloud, corrupted, spell, poison, miasma
- **File:** `sfx/14-spells/plague-cloud.sb`

### `14-spells/shadow-step` — Shadow Step

- **Description:** A short blink through shadow: a falling sweep, a puff of noise and a low pop.
- **Use when:** A short-range teleport or evasive blink.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.28s
- **Sonic profile:** Short (0.28s), dark, bass-heavy; voices: pulse wave, sine, noise; pitch falls, noisy/breathy.
- **Tags:** spells, shadow, step, corrupted, spell, blink, teleport, dodge
- **File:** `sfx/14-spells/shadow-step.sb`

### `14-spells/soul-drain` — Soul Drain

- **Description:** A tendril pulling life: a falling inharmonic tone and a rising inhale of noise.
- **Use when:** The player or an enemy casts soul-drain or life-steal.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.15s
- **Sonic profile:** Medium (1.15s), very dark, bass-present; voices: FM bell/e-piano tone, noise; pitch rises, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** spells, soul, drain, corrupted, spell, life steal, cast
- **File:** `sfx/14-spells/soul-drain.sb`

### `14-spells/spectral-blade` — Spectral Blade

- **Description:** A ghostly slash: a noise whoosh and a ringing inharmonic bell tail.
- **Use when:** A spirit weapon or spectral blade attack.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.05s
- **Sonic profile:** Medium (1.05s), very bright, light low end; voices: FM bell/e-piano tone, noise; pitch falls, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** spells, spectral, blade, corrupted, spell, slash, melee, ghost
- **File:** `sfx/14-spells/spectral-blade.sb`

### `14-spells/spirit-lance` — Spirit Lance

- **Description:** A piercing beam of spirit light: a fast falling pulse zip and a clean bell ring.
- **Use when:** The player casts a pure spirit projectile or lance.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 0.95s
- **Sonic profile:** Medium (0.95s), bright, light low end; voices: pulse wave, FM bell/e-piano tone; pitch falls, echoing tail.
- **Tags:** spells, spirit, lance, pure, spell, spirit light, projectile, cast
- **File:** `sfx/14-spells/spirit-lance.sb`

### `14-spells/void-bolt` — Void Bolt

- **Description:** A dark projectile: a falling inharmonic FM tone over a tremoloing noise rush.
- **Use when:** Casting or impacting a void or shadow bolt.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.4s
- **Sonic profile:** Short (0.40s), very dark, bass-present; voices: FM bell/e-piano tone, noise; pitch falls, tremolo pulsing, noisy/breathy.
- **Tags:** spells, void, bolt, corrupted, spell, projectile, shadow, cast
- **File:** `sfx/14-spells/void-bolt.sb`

### `14-spells/ward-barrier` — Ward Barrier

- **Description:** A protective dome forming: an organ swell and a shimmering bell arpeggio.
- **Use when:** Casting a ward, barrier or shield spell.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), mid, light low end; voices: FM bell/e-piano tone, organ; tremolo pulsing, echoing tail.
- **Tags:** spells, ward, barrier, pure, spell, shield, defense
- **File:** `sfx/14-spells/ward-barrier.sb`

## Enemies & creatures (`15-enemies`)

Enemy vocalisations, movement, spawn/death and boss moments.

### `15-enemies/beast-growl` — Beast Growl

- **Description:** A deep, vibrating growl: detuned low saw with a fast wobble and a rough noise bed.
- **Use when:** A corrupted beast growls, idles or begins an attack.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.9s
- **Sonic profile:** Medium (0.90s), very dark, bass-heavy; voices: sawtooth, noise; vibrato, tremolo pulsing, detuned/chorused, noisy/breathy.
- **Tags:** enemies, beast, growl, corrupted, enemy, creature
- **File:** `sfx/15-enemies/beast-growl.sb`

### `15-enemies/beast-snarl` — Beast Snarl

- **Description:** A short snarl: a rough saw bark with a noise burst.
- **Use when:** A corrupted beast bites or lunges.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), very dark, bass-heavy; voices: sawtooth, noise; vibrato, detuned/chorused, noisy/breathy.
- **Tags:** enemies, beast, snarl, corrupted, enemy, bite, attack
- **File:** `sfx/15-enemies/beast-snarl.sb`

### `15-enemies/bone-rattle` — Bone Rattle

- **Description:** A dry clatter: a quick cluster of high crushed noise ticks.
- **Use when:** Skeletons move, bone constructs assemble, or a bone trap triggers.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.22s
- **Sonic profile:** Short (0.22s), mid, light low end; voices: noise; bitcrushed, noisy/breathy.
- **Tags:** enemies, bone, rattle, corrupted, enemy, skeleton, clatter
- **File:** `sfx/15-enemies/bone-rattle.sb`

### `15-enemies/boss-collapse` — Boss Collapse

- **Description:** A boss falls apart: staggered blasts, a long falling tone and a rolling rumble.
- **Use when:** A boss is defeated.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 3.2s
- **Sonic profile:** Long (3.20s), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, noise; pitch falls, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** enemies, boss, collapse, corrupted, defeat, death
- **File:** `sfx/15-enemies/boss-collapse.sb`

### `15-enemies/boss-intro` — Boss Intro

- **Description:** A boss appears: a deep boom, a toll of a dark bell and a dissonant organ stab.
- **Use when:** A boss encounter begins; use over the title card or entrance.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 2.45s
- **Sonic profile:** Long (2.45s), dark, bass-present; voices: sawtooth, sine, FM bell/e-piano tone; pitch falls, detuned/chorused, echoing tail.
- **Tags:** enemies, boss, intro, corrupted, entrance, sting
- **File:** `sfx/15-enemies/boss-intro.sb`

### `15-enemies/boss-surge` — Boss Surge

- **Description:** A boss powers up: a rising bitcrushed growl, a rumbling sub and a hard hit.
- **Use when:** A boss changes phase, enrages or the corruption surges.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), very dark, bass-heavy; voices: sawtooth, sine, noise; pitch falls, pitch rises, vibrato, tremolo pulsing, detuned/chorused, bitcrushed, noisy/breathy.
- **Tags:** enemies, boss, surge, corrupted, phase, enrage
- **File:** `sfx/15-enemies/boss-surge.sb`

### `15-enemies/cultist-chant` — Cultist Chant

- **Description:** A dissonant choir: three low organ voices a semitone and a tritone apart, swaying slowly.
- **Use when:** A group of cultists chant (ritual scenes, boss rooms, shrines).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), very dark, light low end; voices: organ; vibrato, tremolo pulsing.
- **Tags:** enemies, cultist, chant, corrupted, enemy, choir, ritual
- **File:** `sfx/15-enemies/cultist-chant.sb`

### `15-enemies/husk-shamble` — Husk Shamble

- **Description:** A heavy, wet step and a dragging scrape.
- **Use when:** A husk or undead walks (loop or trigger per step).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.31s
- **Sonic profile:** Short (0.31s), very dark, bass-heavy; voices: sine, noise; bitcrushed, noisy/breathy.
- **Tags:** enemies, husk, shamble, corrupted, enemy, undead, footstep
- **File:** `sfx/15-enemies/husk-shamble.sb`

### `15-enemies/spawn-from-void` — Spawn From Void

- **Description:** Something arrives: a swell, an inhale of noise and a hollow pop.
- **Use when:** An enemy spawns or materialises from a rift or the void.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.85s
- **Sonic profile:** Medium (0.85s), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, noise; pitch falls, pitch rises, tremolo pulsing, noisy/breathy.
- **Tags:** enemies, spawn, from, void, corrupted, enemy, arrive, rift
- **File:** `sfx/15-enemies/spawn-from-void.sb`

### `15-enemies/spectre-screech` — Spectre Screech

- **Description:** A harsh bitcrushed scream that glides downward.
- **Use when:** A spectre or banshee screeches; also a sharp alert or stun-cry.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.6s
- **Sonic profile:** Medium (0.60s), bright, light low end; voices: sawtooth; pitch falls, vibrato, bitcrushed.
- **Tags:** enemies, spectre, screech, corrupted, enemy, banshee, scream
- **File:** `sfx/15-enemies/spectre-screech.sb`

### `15-enemies/swarm-skitter` — Swarm Skitter

- **Description:** Dozens of tiny feet: rapid high ticks that rise and fall in speed.
- **Use when:** A swarm of insects or small spirits moves nearby.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.42s
- **Sonic profile:** Short (0.42s), mid, light low end; voices: noise; bitcrushed, noisy/breathy.
- **Tags:** enemies, swarm, skitter, corrupted, enemy, insects
- **File:** `sfx/15-enemies/swarm-skitter.sb`

### `15-enemies/undead-groan` — Undead Groan

- **Description:** A low, rattling groan: a drooping saw with a pulsing breath.
- **Use when:** A zombie, husk or other undead notices the player or takes a hit.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.9s
- **Sonic profile:** Medium (0.90s), very dark, bass-heavy; voices: sawtooth, noise; pitch falls, vibrato, tremolo pulsing, detuned/chorused, noisy/breathy.
- **Tags:** enemies, undead, groan, corrupted, enemy, zombie, husk
- **File:** `sfx/15-enemies/undead-groan.sb`

### `15-enemies/vanish-into-smoke` — Vanish Into Smoke

- **Description:** An enemy dissolves: a fading bell and a long dispersing noise sigh.
- **Use when:** An enemy dies by dissolving into smoke or ash (spirit-type death).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), dark, bass-present; voices: FM bell/e-piano tone, noise; pitch falls, pitch rises, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** enemies, vanish, into, smoke, corrupted, enemy, death, dissolve
- **File:** `sfx/15-enemies/vanish-into-smoke.sb`

### `15-enemies/wraith-wail` — Wraith Wail

- **Description:** A haunting wail: a high wavering inharmonic FM voice with a heavy echo.
- **Use when:** A wraith or ghost shrieks, spots the player or attacks.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.7s
- **Sonic profile:** Long (1.70s), mid, light low end; voices: FM bell/e-piano tone, noise; pitch falls, vibrato, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** enemies, wraith, wail, corrupted, enemy, ghost, scream
- **File:** `sfx/15-enemies/wraith-wail.sb`

## Realm & objects (`16-realm`)

Rifts, shrines, gates, relics, crystals and other world objects.

### `16-realm/crystal-chime-1` — Crystal Chime 1

- **Description:** Glassy crystal chime #1: a clean high FM ping with a long echoing tail. Variant 1 of 3 (different pitch).
- **Use when:** A spirit crystal is struck, brushed past or breaks into light; pick randomly among crystal-chime-1..3.
- **Palette:** pure · **Zone:** crystal-depths · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), mid, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** realm, crystal, chime, pure, ping, variant
- **File:** `sfx/16-realm/crystal-chime-1.sb`

### `16-realm/crystal-chime-2` — Crystal Chime 2

- **Description:** Glassy crystal chime #2: a clean high FM ping with a long echoing tail. Variant 2 of 3 (different pitch).
- **Use when:** A spirit crystal is struck, brushed past or breaks into light; pick randomly among crystal-chime-1..3.
- **Palette:** pure · **Zone:** crystal-depths · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** realm, crystal, chime, pure, ping, variant
- **File:** `sfx/16-realm/crystal-chime-2.sb`

### `16-realm/crystal-chime-3` — Crystal Chime 3

- **Description:** Glassy crystal chime #3: a clean high FM ping with a long echoing tail. Variant 3 of 3 (different pitch).
- **Use when:** A spirit crystal is struck, brushed past or breaks into light; pick randomly among crystal-chime-1..3.
- **Palette:** pure · **Zone:** crystal-depths · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** realm, crystal, chime, pure, ping, variant
- **File:** `sfx/16-realm/crystal-chime-3.sb`

### `16-realm/cursed-chest-open` — Cursed Chest Open

- **Description:** A chest opens with malice: a groaning creak, a dark bell and a whisper of breath.
- **Use when:** Opening a cursed or trapped chest; also good for unsettling loot.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), bright, light low end; voices: sawtooth, FM bell/e-piano tone, noise; pitch rises, vibrato, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** realm, cursed, chest, open, corrupted, loot, trap
- **File:** `sfx/16-realm/cursed-chest-open.sb`

### `16-realm/lantern-light` — Lantern Light

- **Description:** A spirit lantern ignites: a soft flame whoosh, warm organ and two gentle bells.
- **Use when:** The player lights a spirit lantern or rests at a save point.
- **Palette:** pure · **Zone:** sanctuary · **Theme fit:** core · **Duration:** 1.65s
- **Sonic profile:** Long (1.65s), mid, light low end; voices: FM bell/e-piano tone, organ, noise; pitch rises, echoing tail, noisy/breathy.
- **Tags:** realm, lantern, light, pure, save point, rest, checkpoint
- **File:** `sfx/16-realm/lantern-light.sb`

### `16-realm/lore-tablet` — Lore Tablet

- **Description:** Ancient stone stirring: a grinding scrape, a low bell and a half-heard whisper.
- **Use when:** The player activates or reads a lore tablet or rune stone.
- **Palette:** neutral · **Zone:** ashen-citadel · **Theme fit:** core · **Duration:** 1.8s
- **Sonic profile:** Long (1.80s), dark, light low end; voices: FM bell/e-piano tone, noise; tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** realm, lore, tablet, neutral, rune, read
- **File:** `sfx/16-realm/lore-tablet.sb`

### `16-realm/relic-pickup` — Relic Pickup

- **Description:** A heavy ancient thing is lifted: a low thump, a dark bell and a warm organ glow.
- **Use when:** The player picks up a relic, key artefact or quest item.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 1.4s
- **Sonic profile:** Medium (1.40s), mid, light low end; voices: sine, FM bell/e-piano tone, organ; pitch falls, detuned/chorused, echoing tail.
- **Tags:** realm, relic, pickup, neutral, artifact, quest item
- **File:** `sfx/16-realm/relic-pickup.sb`

### `16-realm/relic-resonance` — Relic Resonance

- **Description:** A relic hums near its place: a pulsing FM tone that slowly swells.
- **Use when:** A relic or key item resonates when the player is near its altar or target.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 2.0s
- **Sonic profile:** Long (2.00s), very dark, light low end; voices: FM bell/e-piano tone; vibrato, tremolo pulsing, echoing tail.
- **Tags:** realm, relic, resonance, neutral, hum, proximity, hint
- **File:** `sfx/16-realm/relic-resonance.sb`

### `16-realm/rift-close` — Rift Close

- **Description:** The veil mends: a falling swell that collapses into a hollow thump.
- **Use when:** A rift or portal closes.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.75s
- **Sonic profile:** Medium (0.75s), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, noise; pitch falls, noisy/breathy.
- **Tags:** realm, rift, close, corrupted, portal, veil
- **File:** `sfx/16-realm/rift-close.sb`

### `16-realm/rift-open` — Rift Open

- **Description:** The veil tears: ripping noise, a rising inharmonic swell and a deep boom.
- **Use when:** A rift, portal or tear in the veil opens.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.1s
- **Sonic profile:** Medium (1.10s), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, noise; pitch falls, pitch rises, tremolo pulsing, noisy/breathy.
- **Tags:** realm, rift, open, corrupted, portal, veil, tear
- **File:** `sfx/16-realm/rift-open.sb`

### `16-realm/shrine-activate` — Shrine Activate

- **Description:** A shrine awakens: a clean bell chord over a swelling organ and a soft sine bloom.
- **Use when:** The player activates a shrine, altar or spirit fountain.
- **Palette:** pure · **Zone:** sanctuary · **Theme fit:** core · **Duration:** 1.7s
- **Sonic profile:** Long (1.70s), dark, light low end; voices: sine, FM bell/e-piano tone, organ; echoing tail.
- **Tags:** realm, shrine, activate, pure, altar, blessing
- **File:** `sfx/16-realm/shrine-activate.sb`

### `16-realm/spirit-gate-open` — Spirit Gate Open

- **Description:** A great gate opening: a grinding rumble that resolves into rising pure bells.
- **Use when:** A spirit gate or sealed door opens after a puzzle or boss.
- **Palette:** neutral · **Zone:** any · **Theme fit:** core · **Duration:** 2.2s
- **Sonic profile:** Long (2.20s), dark, bass-present; voices: sawtooth, FM bell/e-piano tone, noise; pitch rises, vibrato, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** realm, spirit, gate, open, neutral, door, puzzle, boss door
- **File:** `sfx/16-realm/spirit-gate-open.sb`

### `16-realm/veil-pass` — Veil Pass

- **Description:** Passing through the veil: a soft shimmering pulse sweep with a breath of noise.
- **Use when:** The player walks through a veil barrier or a spirit-only passage.
- **Palette:** pure · **Zone:** any · **Theme fit:** core · **Duration:** 1.1s
- **Sonic profile:** Medium (1.10s), mid, light low end; voices: pulse wave, noise; pitch rises, tremolo pulsing, sweeping pulse width, echoing tail, noisy/breathy.
- **Tags:** realm, veil, pass, pure, barrier, spirit form
- **File:** `sfx/16-realm/veil-pass.sb`

## Zones & ambience (`17-zones`)

Per-zone ambience loops, entry stings and one-shots for the six zones.

### `17-zones/amb-ashen-citadel` — Amb Ashen Citadel

- **Description:** Ruined stone city ambience: cavernous organ drone, a distant dark bell tolling, groaning metal and cold wind. 12-second seamless loop.
- **Use when:** Background loop for the Ashen Citadel zone.
- **Palette:** corrupted · **Zone:** ashen-citadel · **Theme fit:** core · **Duration:** 11.5s · loops seamlessly (fade 0.5s)
- **Sonic profile:** Long (11.50s, loops seamlessly), very dark, bass-present; voices: sawtooth, FM bell/e-piano tone, organ, noise; pitch rises, vibrato, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** zones, amb, ashen, citadel, corrupted, ambience, loop, ruins, stone, bell, echo
- **File:** `sfx/17-zones/amb-ashen-citadel.sb`

### `17-zones/amb-crystal-depths` — Amb Crystal Depths

- **Description:** Cavern of resonant crystal: a shimmering FM hum, a deep sub, and sparse high pings with long echoes. 12-second seamless loop.
- **Use when:** Background loop for the Crystal Depths zone.
- **Palette:** pure · **Zone:** crystal-depths · **Theme fit:** core · **Duration:** 11.5s · loops seamlessly (fade 0.5s)
- **Sonic profile:** Long (11.50s, loops seamlessly), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, noise; vibrato, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** zones, amb, crystal, depths, pure, ambience, loop, cave, shimmer, resonance
- **File:** `sfx/17-zones/amb-crystal-depths.sb`

### `17-zones/amb-hollow-wood` — Amb Hollow Wood

- **Description:** Dead-forest ambience: dry wind rushing through bone trees, slow creaks, distant detuned wind-chime ticks and whispers. 12-second seamless loop.
- **Use when:** Background loop for the Hollow Wood zone.
- **Palette:** corrupted · **Zone:** hollow-wood · **Theme fit:** core · **Duration:** 11.5s · loops seamlessly (fade 0.5s)
- **Sonic profile:** Long (11.50s, loops seamlessly), very dark, bass-heavy; voices: sawtooth, sine, FM bell/e-piano tone, noise; pitch rises, vibrato, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** zones, amb, hollow, wood, corrupted, ambience, loop, forest, wind, creak, eerie
- **File:** `sfx/17-zones/amb-hollow-wood.sb`

### `17-zones/amb-rotted-heart` — Amb Rotted Heart

- **Description:** The source of corruption: a slow heartbeat, a huge dissonant drone, a faint cluster of choir tones and sparse bitcrushed glitch bursts. 12-second seamless loop.
- **Use when:** Background loop for the Rotted Heart zone (final area).
- **Palette:** corrupted · **Zone:** rotted-heart · **Theme fit:** core · **Duration:** 11.5s · loops seamlessly (fade 0.5s)
- **Sonic profile:** Long (11.50s, loops seamlessly), very dark, bass-heavy; voices: sawtooth, sine, FM bell/e-piano tone, organ, noise; pitch falls, vibrato, tremolo pulsing, detuned/chorused, bitcrushed, noisy/breathy.
- **Tags:** zones, amb, rotted, heart, corrupted, ambience, loop, corruption, final area, dread
- **File:** `sfx/17-zones/amb-rotted-heart.sb`

### `17-zones/amb-sanctuary` — Amb Sanctuary

- **Description:** Calm, safe ambience: a warm organ fifth with slow shimmer, faint breath of air and sparse clean bell tones. 12-second seamless loop.
- **Use when:** Background loop for the Veil Haven hub and other safe spirit-light areas.
- **Palette:** pure · **Zone:** sanctuary · **Theme fit:** core · **Duration:** 11.5s · loops seamlessly (fade 0.5s)
- **Sonic profile:** Long (11.50s, loops seamlessly), dark, light low end; voices: FM bell/e-piano tone, organ, noise; vibrato, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** zones, amb, sanctuary, pure, ambience, loop, safe, calm, hub
- **File:** `sfx/17-zones/amb-sanctuary.sb`

### `17-zones/amb-weeping-marsh` — Amb Weeping Marsh

- **Description:** Flooded wetland ambience: heavy low drone, slow dripping with long echoes, gloopy bubbles and a sour wobbling undertone. 12-second seamless loop.
- **Use when:** Background loop for the Weeping Marsh zone.
- **Palette:** corrupted · **Zone:** weeping-marsh · **Theme fit:** core · **Duration:** 11.5s · loops seamlessly (fade 0.5s)
- **Sonic profile:** Long (11.50s, loops seamlessly), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, organ, noise; pitch falls, pitch rises, vibrato, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** zones, amb, weeping, marsh, corrupted, ambience, loop, swamp, water, drip, bubbles
- **File:** `sfx/17-zones/amb-weeping-marsh.sb`

### `17-zones/bog-bubble` — Bog Bubble

- **Description:** A heavy bog bubble rising and popping.
- **Use when:** Ambient one-shot in the Weeping Marsh, or a trigger when walking through bog.
- **Palette:** corrupted · **Zone:** weeping-marsh · **Theme fit:** core · **Duration:** 0.17s
- **Sonic profile:** Short (0.17s), very dark, light low end; voices: sine, noise; pitch rises, vibrato, noisy/breathy.
- **Tags:** zones, bog, bubble, corrupted, marsh, ambience
- **File:** `sfx/17-zones/bog-bubble.sb`

### `17-zones/branch-creak` — Branch Creak

- **Description:** A dry wooden creak: a short wobbling groan.
- **Use when:** A bone-tree branch bends or breaks nearby; ambient one-shot for the Hollow Wood.
- **Palette:** corrupted · **Zone:** hollow-wood · **Theme fit:** core · **Duration:** 0.45s
- **Sonic profile:** Short (0.45s), very dark, light low end; voices: sawtooth, noise; pitch rises, vibrato, noisy/breathy.
- **Tags:** zones, branch, creak, corrupted, forest, ambience
- **File:** `sfx/17-zones/branch-creak.sb`

### `17-zones/crystal-ping` — Crystal Ping

- **Description:** A single high crystal ping with a shimmering tail.
- **Use when:** Ambient one-shot in the Crystal Depths, or feedback when a crystal puzzle is solved.
- **Palette:** pure · **Zone:** crystal-depths · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), bright, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** zones, crystal, ping, pure, ambience, puzzle
- **File:** `sfx/17-zones/crystal-ping.sb`

### `17-zones/distant-toll` — Distant Toll

- **Description:** A far-off dark bell with a long, shadowy echo.
- **Use when:** Ambient one-shot in the Ashen Citadel, or a clock/alarm that something is coming.
- **Palette:** corrupted · **Zone:** ashen-citadel · **Theme fit:** core · **Duration:** 3.5s
- **Sonic profile:** Long (3.50s), mid, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail.
- **Tags:** zones, distant, toll, corrupted, citadel, bell, ambience
- **File:** `sfx/17-zones/distant-toll.sb`

### `17-zones/enter-ashen-citadel` — Enter Ashen Citadel

- **Description:** A dead city greets you: a deep stone boom, a distant dark bell toll and cold wind.
- **Use when:** The player enters the Ashen Citadel.
- **Palette:** corrupted · **Zone:** ashen-citadel · **Theme fit:** core · **Duration:** 2.6s
- **Sonic profile:** Long (2.60s), dark, bass-present; voices: sine, FM bell/e-piano tone, noise; pitch falls, tremolo pulsing, detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** zones, enter, ashen, citadel, corrupted, zone entry, sting, ashen-citadel
- **File:** `sfx/17-zones/enter-ashen-citadel.sb`

### `17-zones/enter-crystal-depths` — Enter Crystal Depths

- **Description:** Glass and light: a falling sparkle of bells over a resonant hum.
- **Use when:** The player enters the Crystal Depths.
- **Palette:** pure · **Zone:** crystal-depths · **Theme fit:** core · **Duration:** 2.0s
- **Sonic profile:** Long (2.00s), mid, light low end; voices: FM bell/e-piano tone; tremolo pulsing, echoing tail.
- **Tags:** zones, enter, crystal, depths, pure, zone entry, sting, crystal-depths
- **File:** `sfx/17-zones/enter-crystal-depths.sb`

### `17-zones/enter-hollow-wood` — Enter Hollow Wood

- **Description:** A cold gust and a creak: swelling wind noise, a hollow knock and a distant whisper.
- **Use when:** The player enters the Hollow Wood.
- **Palette:** corrupted · **Zone:** hollow-wood · **Theme fit:** core · **Duration:** 2.0s
- **Sonic profile:** Long (2.00s), dark, light low end; voices: triangle wave, sawtooth, noise; pitch rises, vibrato, tremolo pulsing, echoing tail, noisy/breathy.
- **Tags:** zones, enter, hollow, wood, corrupted, zone entry, sting, hollow-wood
- **File:** `sfx/17-zones/enter-hollow-wood.sb`

### `17-zones/enter-rotted-heart` — Enter Rotted Heart

- **Description:** Dread: a heartbeat, a dissonant swell, a bitcrushed glitch burst and a sub drop.
- **Use when:** The player enters the Rotted Heart.
- **Palette:** corrupted · **Zone:** rotted-heart · **Theme fit:** core · **Duration:** 1.8s
- **Sonic profile:** Long (1.80s), very dark, bass-heavy; voices: sine, FM bell/e-piano tone, noise; pitch falls, detuned/chorused, bitcrushed, noisy/breathy.
- **Tags:** zones, enter, rotted, heart, corrupted, zone entry, sting, rotted-heart
- **File:** `sfx/17-zones/enter-rotted-heart.sb`

### `17-zones/enter-sanctuary` — Enter Sanctuary

- **Description:** A warm welcome: clean bells rising over a soft organ chord.
- **Use when:** The player enters the Veil Haven.
- **Palette:** pure · **Zone:** sanctuary · **Theme fit:** core · **Duration:** 2.1s
- **Sonic profile:** Long (2.10s), dark, light low end; voices: FM bell/e-piano tone, organ; echoing tail.
- **Tags:** zones, enter, sanctuary, pure, zone entry, sting
- **File:** `sfx/17-zones/enter-sanctuary.sb`

### `17-zones/enter-weeping-marsh` — Enter Weeping Marsh

- **Description:** Sinking in: gloopy bubbles, a sagging low drone and a single echoing drip.
- **Use when:** The player enters the Weeping Marsh.
- **Palette:** corrupted · **Zone:** weeping-marsh · **Theme fit:** core · **Duration:** 1.9s
- **Sonic profile:** Long (1.90s), very dark, bass-heavy; voices: sine, FM bell/e-piano tone; pitch falls, pitch rises, vibrato, echoing tail.
- **Tags:** zones, enter, weeping, marsh, corrupted, zone entry, sting, weeping-marsh
- **File:** `sfx/17-zones/enter-weeping-marsh.sb`

### `17-zones/glitch-burst` — Glitch Burst

- **Description:** A burst of bitcrushed digital-sounding static and a stuttering pitch fall.
- **Use when:** Reality tears in the Rotted Heart, or a corruption 'glitch' event.
- **Palette:** corrupted · **Zone:** rotted-heart · **Theme fit:** core · **Duration:** 0.3s
- **Sonic profile:** Short (0.30s), dark, bass-present; voices: pulse wave, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** zones, glitch, burst, corrupted, heart, bitcrush, static
- **File:** `sfx/17-zones/glitch-burst.sb`

### `17-zones/heart-thump` — Heart Thump

- **Description:** One enormous, slow heartbeat: a deep double thump shaking the floor.
- **Use when:** A pulse of corruption in the Rotted Heart; sync to screen shake.
- **Palette:** corrupted · **Zone:** rotted-heart · **Theme fit:** core · **Duration:** 0.53s
- **Sonic profile:** Medium (0.53s), very dark, bass-heavy; voices: sine, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** zones, heart, thump, corrupted, pulse, corruption, shake
- **File:** `sfx/17-zones/heart-thump.sb`

### `17-zones/sanctuary-chime` — Sanctuary Chime

- **Description:** A soft pure bell with a gentle echo.
- **Use when:** A calm ambient one-shot in the Veil Haven, or a gentle reward tone.
- **Palette:** pure · **Zone:** sanctuary · **Theme fit:** core · **Duration:** 1.5s
- **Sonic profile:** Long (1.50s), mid, light low end; voices: FM bell/e-piano tone; echoing tail.
- **Tags:** zones, sanctuary, chime, pure, calm, ambience
- **File:** `sfx/17-zones/sanctuary-chime.sb`

### `17-zones/stone-grind` — Stone Grind

- **Description:** Stone dragging on stone: a low pulsing noise rumble.
- **Use when:** A moving wall, sliding block or falling masonry in the Ashen Citadel.
- **Palette:** corrupted · **Zone:** ashen-citadel · **Theme fit:** core · **Duration:** 0.9s
- **Sonic profile:** Medium (0.90s), very dark, bass-heavy; voices: sine, noise; tremolo pulsing, noisy/breathy.
- **Tags:** zones, stone, grind, corrupted, citadel, puzzle
- **File:** `sfx/17-zones/stone-grind.sb`

### `17-zones/whisper-rustle` — Whisper Rustle

- **Description:** A dry rustle of dead leaves with a hint of voice.
- **Use when:** Ambient one-shot in the Hollow Wood: movement just out of sight.
- **Palette:** corrupted · **Zone:** hollow-wood · **Theme fit:** core · **Duration:** 0.6s
- **Sonic profile:** Medium (0.60s), dark, light low end; voices: noise; pitch rises, tremolo pulsing, noisy/breathy.
- **Tags:** zones, whisper, rustle, corrupted, forest, leaves, ambience
- **File:** `sfx/17-zones/whisper-rustle.sb`

## Corrupted variants (`18-corrupted`)

Corrupted versions of classic pickup, movement and UI sounds, for use inside the realm.

### `18-corrupted/blighted-heart` — Blighted Heart

- **Description:** Health pickup, corrupted: a wobbling low rising figure with a sour detuned tail.
- **Use when:** Picking up a health restore that carries a hint of corruption.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.27s
- **Sonic profile:** Medium (1.27s), very dark, light low end; voices: triangle wave; vibrato, detuned/chorused, echoing tail.
- **Tags:** corrupted, blighted, heart, health, pickup, restore
- **File:** `sfx/18-corrupted/blighted-heart.sb`

### `18-corrupted/corrupted-cancel` — Corrupted Cancel

- **Description:** Menu cancel, corrupted: a falling two-note sour ring.
- **Use when:** Cancelling in a corrupted/dark menu context.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.76s
- **Sonic profile:** Medium (0.76s), bright, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail, bitcrushed.
- **Tags:** corrupted, cancel, ui
- **File:** `sfx/18-corrupted/corrupted-cancel.sb`

### `18-corrupted/corrupted-confirm` — Corrupted Confirm

- **Description:** Menu confirm, corrupted: a rising two-note ring in an inharmonic bell with a crushed edge.
- **Use when:** Confirming a choice in a corrupted/dark menu context.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.76s
- **Sonic profile:** Medium (0.76s), bright, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail, bitcrushed.
- **Tags:** corrupted, confirm, ui
- **File:** `sfx/18-corrupted/corrupted-confirm.sb`

### `18-corrupted/corrupted-footstep-1` — Corrupted Footstep 1

- **Description:** Wet, heavy footstep #1 on corrupted ground: a slap of noise over a squelchy low thump. Variant 1 of 3.
- **Use when:** Footsteps on corrupted ground; pick randomly among corrupted-footstep-1..3 to avoid repetition.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), very dark, bass-heavy; voices: sine, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** corrupted, footstep, corrupted ground, variant, wet
- **File:** `sfx/18-corrupted/corrupted-footstep-1.sb`

### `18-corrupted/corrupted-footstep-2` — Corrupted Footstep 2

- **Description:** Wet, heavy footstep #2 on corrupted ground: a slap of noise over a squelchy low thump. Variant 2 of 3.
- **Use when:** Footsteps on corrupted ground; pick randomly among corrupted-footstep-1..3 to avoid repetition.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), very dark, bass-heavy; voices: sine, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** corrupted, footstep, corrupted ground, variant, wet
- **File:** `sfx/18-corrupted/corrupted-footstep-2.sb`

### `18-corrupted/corrupted-footstep-3` — Corrupted Footstep 3

- **Description:** Wet, heavy footstep #3 on corrupted ground: a slap of noise over a squelchy low thump. Variant 3 of 3.
- **Use when:** Footsteps on corrupted ground; pick randomly among corrupted-footstep-1..3 to avoid repetition.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.1s
- **Sonic profile:** Tick (0.10s), very dark, bass-heavy; voices: sine, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** corrupted, footstep, corrupted ground, variant, wet
- **File:** `sfx/18-corrupted/corrupted-footstep-3.sb`

### `18-corrupted/corrupted-jump` — Corrupted Jump

- **Description:** A sluggish, bent jump: a rising chirp that wobbles and sags.
- **Use when:** Jumping while corrupted or on corrupted ground.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.22s
- **Sonic profile:** Short (0.22s), mid, light low end; voices: pulse wave; pitch rises, vibrato, detuned/chorused.
- **Tags:** corrupted, jump
- **File:** `sfx/18-corrupted/corrupted-jump.sb`

### `18-corrupted/corrupted-land` — Corrupted Land

- **Description:** A squelching landing: a heavy crushed thud with a wet slap.
- **Use when:** Landing on corrupted ground.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.16s
- **Sonic profile:** Short (0.16s), very dark, bass-heavy; voices: sine, noise; pitch falls, bitcrushed, noisy/breathy.
- **Tags:** corrupted, land
- **File:** `sfx/18-corrupted/corrupted-land.sb`

### `18-corrupted/corrupted-level-up` — Corrupted Level Up

- **Description:** Level up, but wrong: a rising scale in a minor mode, wavering and detuned, ending on a hollow bell.
- **Use when:** The player levels up while corrupted, or in the Rotted Heart.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.6s
- **Sonic profile:** Long (1.60s), mid, light low end; voices: pulse wave, FM bell/e-piano tone; vibrato, detuned/chorused, echoing tail.
- **Tags:** corrupted, level, up, level up, progression, dark
- **File:** `sfx/18-corrupted/corrupted-level-up.sb`

### `18-corrupted/corrupted-power-up` — Corrupted Power Up

- **Description:** A buff gained at a cost: a rising run with vibrato that bends sour at the top.
- **Use when:** Gaining a power-up from a corrupt source (dark shrine, cursed item).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), bright, light low end; voices: pulse wave; vibrato, detuned/chorused, echoing tail, bitcrushed.
- **Tags:** corrupted, power, up, buff, power-up, dark
- **File:** `sfx/18-corrupted/corrupted-power-up.sb`

### `18-corrupted/corrupted-save` — Corrupted Save

- **Description:** Save chime, tainted: a falling run of dark bells that leaves a hollow organ tone.
- **Use when:** Saving the game away from sanctuary (corrupted zones).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.3s
- **Sonic profile:** Medium (1.30s), bright, light low end; voices: FM bell/e-piano tone, organ; detuned/chorused, echoing tail.
- **Tags:** corrupted, save, ui, tainted
- **File:** `sfx/18-corrupted/corrupted-save.sb`

### `18-corrupted/rusted-key` — Rusted Key

- **Description:** Key pickup, corrupted: a flat, grinding metallic clank and a dull ring.
- **Use when:** Obtaining a key.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.96s
- **Sonic profile:** Medium (0.96s), very bright, light low end; voices: FM bell/e-piano tone, noise; detuned/chorused, echoing tail, noisy/breathy.
- **Tags:** corrupted, rusted, key, pickup
- **File:** `sfx/18-corrupted/rusted-key.sb`

### `18-corrupted/shard-spend` — Shard Spend

- **Description:** Paying shards: two falling dull clinks.
- **Use when:** Spending soul shards at a vendor.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.81s
- **Sonic profile:** Medium (0.81s), bright, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail.
- **Tags:** corrupted, shard, spend, currency, vendor
- **File:** `sfx/18-corrupted/shard-spend.sb`

### `18-corrupted/soul-shard` — Soul Shard

- **Description:** Currency pickup, corrupted: a detuned, inharmonic two-note ring with a crushed edge.
- **Use when:** Collecting soul shards (the realm's currency). Replaces coin in this setting.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.06s
- **Sonic profile:** Medium (1.06s), very bright, light low end; voices: FM bell/e-piano tone; detuned/chorused, echoing tail, bitcrushed.
- **Tags:** corrupted, soul, shard, currency, pickup, soul shard, coin replacement
- **File:** `sfx/18-corrupted/soul-shard.sb`

### `18-corrupted/tainted-treasure` — Tainted Treasure

- **Description:** A chest opens onto corrupted loot: a groan, then a sour, falling run of bells.
- **Use when:** Opening a regular chest in a corrupted zone.
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 1.55s
- **Sonic profile:** Long (1.55s), very bright, light low end; voices: sawtooth, FM bell/e-piano tone; pitch rises, vibrato, detuned/chorused, echoing tail.
- **Tags:** corrupted, tainted, treasure, chest, loot
- **File:** `sfx/18-corrupted/tainted-treasure.sb`

### `18-corrupted/void-essence` — Void Essence

- **Description:** Mana pickup, corrupted: a swirling, falling pulse sweep with a bitcrushed shimmer.
- **Use when:** Collecting void essence (mana/energy).
- **Palette:** corrupted · **Zone:** any · **Theme fit:** core · **Duration:** 0.9s
- **Sonic profile:** Medium (0.90s), mid, light low end; voices: pulse wave; pitch rises, sweeping pulse width, echoing tail, bitcrushed.
- **Tags:** corrupted, void, essence, mana, pickup, energy
- **File:** `sfx/18-corrupted/void-essence.sb`

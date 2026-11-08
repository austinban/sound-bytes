import unittest

import numpy as np

from sound_bytes.parser import ScoreError, parse_score, pitch_to_midi
from sound_bytes.render import render_score


class ParserTests(unittest.TestCase):
    def test_pitch_to_midi(self):
        self.assertEqual(pitch_to_midi("A4"), 69)
        self.assertEqual(pitch_to_midi("C4"), 60)
        self.assertEqual(pitch_to_midi("C#4"), 61)
        self.assertEqual(pitch_to_midi("Db4"), 61)

    def test_repeat_and_comments(self):
        s = parse_score("instrument a: pulse\na: [C4:1 R:0.5]x3  # comment\n")
        self.assertEqual(len(s.channels["a"]), 6)

    def test_sharp_is_not_a_comment(self):
        s = parse_score("instrument a: pulse\na: C#4:1\n")
        self.assertEqual(s.channels["a"][0].midi, 61)

    def test_errors_have_line_numbers(self):
        with self.assertRaisesRegex(ScoreError, "line 2"):
            parse_score("instrument a: pulse\na: H:1\n")
        with self.assertRaisesRegex(ScoreError, "line 1"):
            parse_score("ghost: C4:1\n")


class SongIOTests(unittest.TestCase):
    def test_round_trip_through_json(self):
        from sound_bytes.songio import json_to_text, score_to_json

        src = open("songs/demo.sb").read()
        first = score_to_json(parse_score(src))
        again = score_to_json(parse_score(json_to_text(first)))
        self.assertEqual(first, again)
        self.assertEqual(first["bars"], 8)

    def test_overlap_rejected(self):
        from sound_bytes.songio import json_to_text

        song = {"title": "t", "tempo": 120, "bars": 1, "tracks": [
            {"name": "a", "wave": "pulse", "params": {},
             "notes": [{"start": 0, "len": 2, "midi": 60}, {"start": 1, "len": 1, "midi": 62}]}]}
        with self.assertRaises(ValueError):
            json_to_text(song)

    def test_preset_reference(self):
        s = parse_score("instrument a: @triangle-bass volume=0.1\na: C3:1\n")
        self.assertEqual(s.instruments["a"].wave, "triangle")
        self.assertEqual(s.instruments["a"].params["volume"], 0.1)


class RenderTests(unittest.TestCase):
    def test_stems_align_and_have_expected_length(self):
        s = parse_score(
            "tempo: 120\ninstrument a: pulse\ninstrument d: noise\n"
            "a: C4:2\nd: K:1 S:2\n"
        )
        stems = render_score(s, sr=8000)
        self.assertEqual(len(stems["a"]), len(stems["d"]))
        self.assertEqual(len(stems["d"]), 8000 * 3 // 2)  # 3 beats @ 120bpm = 1.5s
        self.assertGreater(np.max(np.abs(stems["a"])), 0)


class ShapingTests(unittest.TestCase):
    def _note(self, params, n=8000, sr=8000):
        import numpy as np

        from sound_bytes.parser import Instrument, Note
        from sound_bytes.synth import render_note

        inst = Instrument("a", "pulse", {"volume": 0.5, **params})
        return render_note(inst, Note("pitch", 1.0, midi=69), n, sr, np.random.default_rng(0))

    def test_default_note_is_unchanged_by_new_params_being_absent(self):
        import numpy as np

        self.assertTrue(np.array_equal(self._note({}), self._note({"vibrato": 0, "slide": 0, "pwm": 0, "tremolo": 0})))

    def test_each_shaping_param_changes_the_sound_and_stays_in_range(self):
        import numpy as np

        plain = self._note({})
        for params in ({"vibrato": 40, "vibrato_delay": 0}, {"slide": 12}, {"pwm": 0.3}, {"tremolo": 0.8}):
            shaped = self._note(params)
            self.assertEqual(len(shaped), len(plain))
            self.assertFalse(np.array_equal(shaped, plain), params)
            # volume is 0.5; off-centre pulse duties peak up to 2x after DC removal, so 1.0 is the ceiling
            self.assertLessEqual(float(np.max(np.abs(shaped))), 1.0, params)

    def test_tremolo_dips_the_volume(self):
        import numpy as np

        loud = np.abs(self._note({})).max()
        trough = np.abs(self._note({"tremolo": 1.0, "tremolo_rate": 4})[2900:3100]).max()
        self.assertLess(trough, loud * 0.1)  # at 4Hz the volume bottoms out at t=0.375s (sample 3000 at 8kHz)


class VoiceTests(unittest.TestCase):
    def test_new_voices_render_in_range_and_differ(self):
        import numpy as np

        from sound_bytes.parser import Instrument, Note
        from sound_bytes.synth import render_note

        def render(wave, **params):
            inst = Instrument("a", wave, {"volume": 1.0, **params})
            return render_note(inst, Note("pitch", 1.0, midi=57), 8000, 8000, np.random.default_rng(0))

        outs = {w: render(w, attack=0.0, release=0.0) for w in ("pulse", "triangle", "saw", "sine", "organ", "fm")}
        for name, out in outs.items():
            self.assertTrue(np.all(np.isfinite(out)), name)
            self.assertGreater(float(np.max(np.abs(out))), 0.3, name)
            self.assertLessEqual(float(np.max(np.abs(out))), 1.0001, name)
        names = list(outs)
        for i, x in enumerate(names):
            for y in names[i + 1:]:
                self.assertFalse(np.allclose(outs[x], outs[y]), (x, y))
        # the FM index decays, so a longer fade must change the tone
        self.assertFalse(np.allclose(render("fm", index_decay=0.05), render("fm", index_decay=0.9)))

    def test_parser_accepts_new_voices(self):
        s = parse_score("instrument a: saw\ninstrument b: @bell\ninstrument c: @organ\na: C2:1\nb: C4:1\nc: C3:1\n")
        self.assertEqual([s.instruments[k].wave for k in "abc"], ["saw", "fm", "organ"])


class SfxTests(unittest.TestCase):
    def test_pitched_noise_parses_and_renders(self):
        import numpy as np

        from sound_bytes.render import render_score

        s = parse_score("tempo: 120\ninstrument n: noise volume=0.5 slide=12\nn: C5:1 K:1 R:0.5\n")
        self.assertEqual([n.kind for n in s.channels["n"]], ["pitch", "drum", "rest"])
        out = render_score(s, sr=8000)["n"]
        self.assertGreater(float(np.max(np.abs(out[:4000]))), 0.05)

    def test_every_sound_effect_renders_cleanly(self):
        import numpy as np

        from sound_bytes.sfx import find_sfx, list_sfx, render_sfx

        sounds = list_sfx()
        self.assertGreaterEqual(len(sounds), 100)
        self.assertGreaterEqual(len({s["category"] for s in sounds}), 8)
        self.assertEqual(len({s["id"] for s in sounds}), len(sounds))
        for s in sounds:
            self.assertTrue(s["description"], s["id"])
            out = render_sfx(find_sfx(s["category"], s["name"]), sr=22050)
            self.assertTrue(np.all(np.isfinite(out)), s["id"])
            self.assertGreater(float(np.max(np.abs(out))), 0.02, s["id"])
            self.assertLessEqual(float(np.max(np.abs(out))), 1.0, s["id"])

    def test_find_sfx_rejects_path_tricks(self):
        from sound_bytes.sfx import find_sfx

        self.assertIsNone(find_sfx("..", "x"))
        self.assertIsNone(find_sfx("01-ui", "../../README"))
        self.assertIsNotNone(find_sfx("01-ui", "confirm"))


class SfxMetadataTests(unittest.TestCase):
    def test_every_sound_has_valid_metadata(self):
        from sound_bytes.sfx import list_sfx, load_taxonomy

        tx = load_taxonomy()
        sounds = list_sfx()
        for s in sounds:
            self.assertTrue(s["description"] and s["use_when"] and s["tags"], s["id"])
            self.assertIn(s["palette"], tx["palettes"], s["id"])
            self.assertIn(s["fit"], tx["theme_fit"], s["id"])
            self.assertIn(s["category"], tx["categories"], s["id"])
            self.assertTrue(s["zone"] == "any" or s["zone"] in tx["zones"], s["id"])
        # every zone has an ambience loop and an entry sting
        for zone in tx["zones"]:
            in_zone = [s for s in sounds if s["zone"] == zone]
            self.assertTrue(any(s["loop"] for s in in_zone), f"{zone}: no ambience loop")
            self.assertTrue(any(s["name"] == f"enter-{zone}" for s in in_zone), f"{zone}: no entry sting")

    def test_loops_wrap_without_a_click(self):
        import numpy as np

        from sound_bytes.sfx import find_sfx, list_sfx, render_sfx

        loops = [s for s in list_sfx() if s["loop"]]
        self.assertGreaterEqual(len(loops), 6)
        for s in loops:
            a = render_sfx(find_sfx(s["category"], s["name"]), sr=22050)
            seam = abs(float(a[0]) - float(a[-1]))
            self.assertLess(seam, 10 * float(np.mean(np.abs(np.diff(a)))) + 1e-3, s["id"])  # no jump bigger than normal sample-to-sample change
            self.assertGreater(float(np.sqrt((a[: len(a) // 2] ** 2).mean())), 0.02, s["id"])

    def test_catalog_matches_the_sound_files(self):
        import json

        from sound_bytes.sfx import SFX_DIR, list_sfx

        cat = json.loads((SFX_DIR / "catalog.json").read_text())
        on_disk = {s["id"]: s for s in list_sfx()}
        self.assertEqual({s["id"] for s in cat["sounds"]}, set(on_disk), "catalog is stale: run python3 -m sound_bytes.sfx --catalog")
        for s in cat["sounds"]:
            d = on_disk[s["id"]]
            self.assertEqual((s["description"], s["use_when"], s["palette"], s["zone"], s["theme_fit"], s["tags"]),
                             (d["description"], d["use_when"], d["palette"], d["zone"], d["fit"], d["tags"]), s["id"])
            self.assertTrue(s["profile"]["summary"])

    def test_every_sound_id_in_the_guide_exists(self):
        import json
        import re
        from pathlib import Path

        from sound_bytes.sfx import SFX_DIR

        guide = (Path(SFX_DIR).parent / "SOUND_EFFECTS_GUIDE.md").read_text()
        ids = {s["id"] for s in json.loads((SFX_DIR / "catalog.json").read_text())["sounds"]}
        mentioned = set(re.findall(r"`(\d\d-[a-z]+(?:-[a-z]+)*/[a-z0-9]+(?:-[a-z0-9]+)*)`", guide))
        self.assertGreater(len(mentioned), 40)
        self.assertEqual(sorted(m for m in mentioned if m not in ids), [])
        self.assertIn(f"{len(ids)} ", guide)  # the sound count quoted in the guide is current

    def test_bitcrush_and_hold_change_the_sound(self):
        import numpy as np

        from sound_bytes.parser import Instrument, Note
        from sound_bytes.synth import render_note

        def render(**params):
            inst = Instrument("a", "sine", {"volume": 0.5, **params})
            return render_note(inst, Note("pitch", 1.0, midi=57), 4000, 8000, np.random.default_rng(0))

        plain = render()
        crushed = render(bits=3)
        self.assertLessEqual(len(np.unique(np.round(crushed, 6))), 8)   # 3 bits -> at most 8 amplitude levels
        self.assertFalse(np.allclose(plain, crushed))
        held = render(hold=4)
        self.assertTrue(np.array_equal(held[0:4], np.repeat(held[0], 4)))


class Mp3Tests(unittest.TestCase):
    def test_mp3_export_writes_valid_file(self):
        try:
            import lameenc  # noqa: F401
        except ImportError:
            self.skipTest("lameenc not installed")
        import tempfile
        from pathlib import Path

        from sound_bytes.render import render_to_dir

        s = parse_score("tempo: 120\ninstrument a: pulse\na: C4:2\n")
        with tempfile.TemporaryDirectory() as d:
            paths = render_to_dir(s, Path(d), sr=44100, formats=("mp3",))
            data = paths["mix"][0].read_bytes()
            self.assertGreater(len(data), 1000)
            self.assertTrue(data[:3] == b"ID3" or data[0] == 0xFF)  # ID3 tag or MPEG frame sync


if __name__ == "__main__":
    unittest.main()

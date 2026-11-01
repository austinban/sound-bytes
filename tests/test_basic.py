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


if __name__ == "__main__":
    unittest.main()

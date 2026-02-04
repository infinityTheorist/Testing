"""Tests for HUD parsing."""

import unittest

from smap.observation import HudState
from smap.vision.hud import parse_hud


def make_blank_frame(width: int = 2, height: int = 2):
    return [[(0, 0, 0) for _ in range(width)] for _ in range(height)]


class TestHudParser(unittest.TestCase):
    def test_parse_hud_returns_defaults(self) -> None:
        frame = make_blank_frame()
        hud = parse_hud(frame)
        self.assertIsInstance(hud, HudState)
        self.assertEqual(hud.energy, 99)
        self.assertEqual(hud.missiles, 0)
        self.assertEqual(hud.items, set())


if __name__ == "__main__":
    unittest.main()

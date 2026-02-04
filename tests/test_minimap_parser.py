"""Tests for minimap parsing."""

import unittest

from smap.observation import MinimapState
from smap.vision.minimap import parse_minimap


def make_blank_frame(width: int = 2, height: int = 2):
    return [[(0, 0, 0) for _ in range(width)] for _ in range(height)]


class TestMinimapParser(unittest.TestCase):
    def test_parse_minimap_returns_defaults(self) -> None:
        frame = make_blank_frame()
        minimap = parse_minimap(frame)
        self.assertIsInstance(minimap, MinimapState)
        self.assertEqual(minimap.revealed_tiles, set())
        self.assertIsNone(minimap.player_tile)


if __name__ == "__main__":
    unittest.main()

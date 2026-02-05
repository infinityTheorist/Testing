"""Minimap parsing utilities.

This stub returns empty map state until pixel parsing is implemented.
"""

from __future__ import annotations

from typing import Sequence, Tuple

from smap.observation import MinimapState

RGB = Tuple[int, int, int]
Frame = Sequence[Sequence[RGB]]


def parse_minimap(frame: Frame) -> MinimapState:
    """Parse revealed tiles and player position from the minimap.

    TODO: Identify minimap region, tile colors, and current position marker.
    """
    _ = frame
    return MinimapState(revealed_tiles=set(), player_tile=None)

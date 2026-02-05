"""HUD parsing utilities.

Pixel parsing should only use frame data. This stub returns defaults until
real digit/icon templates are added.
"""

from __future__ import annotations

from typing import Sequence, Tuple

from smap.observation import HudState

RGB = Tuple[int, int, int]
Frame = Sequence[Sequence[RGB]]


def parse_hud(frame: Frame) -> HudState:
    """Parse the HUD from a video frame.

    TODO: Implement digit template matching or OCR on HUD regions.
    """
    _ = frame
    return HudState(
        energy=99,
        missiles=0,
        supers=0,
        power_bombs=0,
        reserves=0,
        items=set(),
    )

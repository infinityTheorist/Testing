"""Observation models derived from pixel-visible game state."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Optional, Sequence, Set, Tuple

RGB = Tuple[int, int, int]
Frame = Sequence[Sequence[RGB]]


@dataclass(frozen=True)
class HudState:
    energy: int
    missiles: int
    supers: int
    power_bombs: int
    reserves: int
    items: Set[str]


@dataclass(frozen=True)
class MinimapState:
    revealed_tiles: Set[Tuple[int, int]]
    player_tile: Optional[Tuple[int, int]]


@dataclass(frozen=True)
class DoorObservation:
    position: Tuple[int, int]
    color: str
    requires: Optional[str]


@dataclass(frozen=True)
class BossState:
    name: Optional[str]
    hp_ratio: Optional[float]


@dataclass(frozen=True)
class Observation:
    timestamp_s: float
    hud: HudState
    minimap: MinimapState
    doors_seen: Sequence[DoorObservation]
    enemies_seen: Sequence[str]
    boss_state: BossState
    frame: Frame
    metadata: Dict[str, str]

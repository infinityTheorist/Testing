"""Frontier exploration policy skeleton."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from smap.world.graph import KnownWorldGraph


@dataclass
class FrontierObjective:
    room_id: str
    door_direction: str


class FrontierExplorer:
    """Selects frontier doors to explore next."""

    def choose_objective(self, graph: KnownWorldGraph) -> Optional[FrontierObjective]:
        for room_id, door in graph.iter_frontier_doors():
            return FrontierObjective(room_id=room_id, door_direction=door.direction)
        return None

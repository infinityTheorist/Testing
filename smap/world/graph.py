"""Known world graph built from observed rooms and doors."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Optional, Set, Tuple


@dataclass
class DoorInfo:
    direction: str
    color: Optional[str] = None
    requires: Optional[str] = None


@dataclass
class RoomNode:
    room_id: str
    minimap_signature: Tuple[int, ...]
    visual_hash: str
    exits: Dict[str, DoorInfo] = field(default_factory=dict)
    items_seen: Set[str] = field(default_factory=set)


@dataclass(frozen=True)
class RoomEdge:
    from_room: str
    to_room: str
    via: str


class KnownWorldGraph:
    """Graph of known rooms based on observations."""

    def __init__(self) -> None:
        self.rooms: Dict[str, RoomNode] = {}
        self.edges: Dict[str, Set[RoomEdge]] = {}

    def add_room(self, node: RoomNode) -> None:
        if node.room_id not in self.rooms:
            self.rooms[node.room_id] = node
            self.edges[node.room_id] = set()

    def connect(self, from_room: str, to_room: str, via: str) -> None:
        if from_room not in self.rooms or to_room not in self.rooms:
            raise ValueError("Rooms must be added before connecting.")
        edge = RoomEdge(from_room=from_room, to_room=to_room, via=via)
        self.edges[from_room].add(edge)

    def iter_frontier_doors(self) -> Iterable[Tuple[str, DoorInfo]]:
        for room_id, room in self.rooms.items():
            for door_id, door in room.exits.items():
                if door_id not in {edge.via for edge in self.edges[room_id]}:
                    yield room_id, door

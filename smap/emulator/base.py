"""Emulator interface definitions.

The emulator adapter must never expose memory inspection APIs. Only video/audio
frames and controller I/O are allowed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence, Tuple

RGB = Tuple[int, int, int]
Frame = Sequence[Sequence[RGB]]


@dataclass(frozen=True)
class InputState:
    """Represents a controller state for a single frame."""

    up: bool = False
    down: bool = False
    left: bool = False
    right: bool = False
    a: bool = False
    b: bool = False
    x: bool = False
    y: bool = False
    l: bool = False
    r: bool = False
    start: bool = False
    select: bool = False


@dataclass(frozen=True)
class StepResult:
    """Output of stepping the emulator."""

    frame: Frame
    audio_samples: Iterable[float]


class EmulatorInterface:
    """Minimal emulator interface used by the agent."""

    def reset(self) -> None:
        raise NotImplementedError

    def step(self, frames: int, input_state: InputState) -> StepResult:
        """Advance the emulator by N frames with the given input state."""
        raise NotImplementedError

    def close(self) -> None:
        """Release resources."""
        raise NotImplementedError

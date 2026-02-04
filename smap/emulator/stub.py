"""Stub emulator for development/testing without a real emulator backend."""

from __future__ import annotations

import itertools
from typing import Iterable, Sequence, Tuple

from smap.emulator.base import EmulatorInterface, Frame, InputState, StepResult

RGB = Tuple[int, int, int]


class StubEmulator(EmulatorInterface):
    """Returns blank frames and silent audio."""

    def __init__(self, width: int = 256, height: int = 224) -> None:
        self._width = width
        self._height = height
        self._blank_frame: Frame = [
            [(0, 0, 0) for _ in range(self._width)] for _ in range(self._height)
        ]

    def reset(self) -> None:
        return None

    def step(self, frames: int, input_state: InputState) -> StepResult:
        _ = frames
        _ = input_state
        silent_audio: Iterable[float] = itertools.repeat(0.0, 0)
        return StepResult(frame=self._blank_frame, audio_samples=silent_audio)

    def close(self) -> None:
        return None

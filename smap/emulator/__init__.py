"""Emulator adapters."""

from smap.emulator.base import EmulatorInterface, InputState, StepResult
from smap.emulator.stub import StubEmulator

__all__ = ["EmulatorInterface", "InputState", "StepResult", "StubEmulator"]

"""Configuration models for the Super Metroid Auto Player."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RunConfig:
    """Runtime configuration for a run."""

    rom_path: Path
    mode: str
    log_dir: Path
    save_frames: bool = True
    frame_stride: int = 30
    input_latency_frames: int = 0
    fps: int = 60


@dataclass(frozen=True)
class ReplayConfig:
    """Configuration for replaying a run from logs."""

    log_dir: Path
    speed_multiplier: float = 1.0

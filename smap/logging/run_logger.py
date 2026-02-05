"""Logging utilities for runs and deterministic replay."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Optional

from smap.emulator.base import InputState, StepResult
from smap.observation import Observation


@dataclass
class StepLog:
    frame_index: int
    input_state: InputState
    observation: Observation


class RunLogger:
    """Writes log data to disk for replay."""

    def __init__(self, log_dir: Path) -> None:
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self._steps_path = self.log_dir / "steps.jsonl"
        self._steps_file = self._steps_path.open("w", encoding="utf-8")
        self._metadata_path = self.log_dir / "meta.json"

    def write_metadata(self, data: Dict[str, Any]) -> None:
        self._metadata_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def log_step(self, step_log: StepLog) -> None:
        payload = {
            "frame_index": step_log.frame_index,
            "input_state": asdict(step_log.input_state),
            "observation": self._serialize_observation(step_log.observation),
        }
        self._steps_file.write(json.dumps(payload) + "\n")

    def log_frame(self, frame_index: int, step_result: StepResult) -> Optional[Path]:
        """Persist a frame snapshot if a saver is available.

        TODO: add actual frame encoding when a real emulator backend is wired.
        """
        _ = frame_index
        _ = step_result
        return None

    def close(self) -> None:
        self._steps_file.close()

    def _serialize_observation(self, observation: Observation) -> Dict[str, Any]:
        return {
            "timestamp_s": observation.timestamp_s,
            "hud": asdict(observation.hud),
            "minimap": {
                "revealed_tiles": list(observation.minimap.revealed_tiles),
                "player_tile": observation.minimap.player_tile,
            },
            "doors_seen": [asdict(door) for door in observation.doors_seen],
            "enemies_seen": list(observation.enemies_seen),
            "boss_state": asdict(observation.boss_state),
            "metadata": observation.metadata,
        }

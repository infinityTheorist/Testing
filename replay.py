"""Replay a logged run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from smap.config import ReplayConfig


def parse_args() -> ReplayConfig:
    parser = argparse.ArgumentParser(description="Replay a logged run")
    parser.add_argument("--log_dir", required=True, type=Path)
    parser.add_argument("--speed", type=float, default=1.0)
    args = parser.parse_args()
    return ReplayConfig(log_dir=args.log_dir, speed_multiplier=args.speed)


def replay(config: ReplayConfig) -> None:
    steps_path = config.log_dir / "steps.jsonl"
    if not steps_path.exists():
        raise FileNotFoundError(f"Missing steps.jsonl in {config.log_dir}")
    with steps_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            step = json.loads(line)
            print(f"Frame {step['frame_index']}: input={step['input_state']}")


def main() -> None:
    config = parse_args()
    replay(config)


if __name__ == "__main__":
    main()

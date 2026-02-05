"""CLI entrypoint for running the Super Metroid Auto Player."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

from smap.config import RunConfig
from smap.emulator import InputState, StubEmulator
from smap.logging import RunLogger, StepLog
from smap.observation import BossState, DoorObservation, Observation
from smap.vision import parse_hud, parse_minimap


def parse_args() -> RunConfig:
    parser = argparse.ArgumentParser(description="Run the Super Metroid Auto Player")
    parser.add_argument("--rom", required=True, type=Path, help="Path to the ROM file")
    parser.add_argument("--mode", default="race", help="Run mode (race/dev)")
    parser.add_argument("--log_dir", required=True, type=Path, help="Log directory")
    parser.add_argument("--no_frames", action="store_true", help="Disable frame saving")
    parser.add_argument("--frame_stride", type=int, default=30)
    parser.add_argument("--input_latency", type=int, default=0)
    parser.add_argument("--fps", type=int, default=60)
    args = parser.parse_args()
    return RunConfig(
        rom_path=args.rom,
        mode=args.mode,
        log_dir=args.log_dir,
        save_frames=not args.no_frames,
        frame_stride=args.frame_stride,
        input_latency_frames=args.input_latency,
        fps=args.fps,
    )


def run_loop(config: RunConfig) -> None:
    emulator = StubEmulator()
    logger = RunLogger(config.log_dir)
    logger.write_metadata(
        {
            "rom": str(config.rom_path),
            "mode": config.mode,
            "fps": config.fps,
            "input_latency_frames": config.input_latency_frames,
        }
    )

    try:
        emulator.reset()
        for frame_index in range(120):
            input_state = InputState()
            step_result = emulator.step(frames=1, input_state=input_state)
            hud_state = parse_hud(step_result.frame)
            minimap_state = parse_minimap(step_result.frame)
            observation = Observation(
                timestamp_s=time.time(),
                hud=hud_state,
                minimap=minimap_state,
                doors_seen=[],
                enemies_seen=[],
                boss_state=BossState(name=None, hp_ratio=None),
                frame=step_result.frame,
                metadata={"note": "stub run"},
            )
            logger.log_step(StepLog(frame_index=frame_index, input_state=input_state, observation=observation))
            if config.save_frames and frame_index % config.frame_stride == 0:
                logger.log_frame(frame_index, step_result)
    finally:
        emulator.close()
        logger.close()


def main() -> None:
    config = parse_args()
    run_loop(config)


if __name__ == "__main__":
    main()

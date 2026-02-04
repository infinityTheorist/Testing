# Super Metroid Auto Player (Map Rando)

This repository contains an early-stage, **no-oracle** Super Metroid auto player
focused on maprando.com seeds. The agent only uses emulator video/audio frames
and controller input/output. It **never** reads emulator RAM or hidden state.

See [docs/NO_ORACLE.md](docs/NO_ORACLE.md) for the strict boundary definition.

## Emulator Strategy (Initial)

**Recommended approach:** **BizHawk + Lua bridge (later)**

- BizHawk provides mature scripting hooks for frame stepping, deterministic
  replay, and video/audio capture.
- Lua scripts can expose only the pixel framebuffer and controller I/O to the
  Python agent, which helps enforce the no-oracle boundary.
- The integration can be swapped later for libretro/RetroArch if desired.

The current implementation ships a **StubEmulator** for Phase 0/1 scaffolding.

## Repo Layout

- `smap/emulator/`: emulator interface + stub backend
- `smap/vision/`: HUD/minimap parsing stubs
- `smap/world/`: known-world graph
- `smap/policy/`: frontier exploration policy
- `smap/logging/`: run logging + replay metadata
- `run.py`: run entrypoint
- `replay.py`: replay entrypoint
- `tests/`: parser test scaffolding

## Quick Start (Windows)

> Requires Python 3.10+.

1. **Clone the repo**
   ```powershell
   git clone <repo-url>
   cd Testing
   ```
2. **Create a virtual environment**
   ```powershell
   py -3.10 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. **Run the stub loop**
   ```powershell
   python run.py --rom path\to\seed.sfc --mode race --log_dir runs\seed123
   ```
4. **Replay the log**
   ```powershell
   python replay.py --log_dir runs\seed123
   ```

## Next Steps

- Replace `StubEmulator` with a BizHawk adapter that captures frames and accepts
  controller inputs.
- Implement HUD and minimap parsing in `smap/vision/`.
- Grow the world graph and frontier exploration policy.

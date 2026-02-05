# No-Oracle Boundary

This project enforces a **human-visible-only** constraint:

- The agent may use emulator video frames, audio (optional), and controller I/O.
- The agent must **not** read emulator RAM or any hidden state such as room IDs,
  coordinates, map layout, item flags, RNG state, or door requirements.
- Knowledge is built only from pixels on screen (HUD, minimap, map station
  display, door sprites, boss HP bars, etc.).
- The agent may keep its own internal memory of rooms/items it has actually
  observed.

The emulator adapter interface (`smap.emulator.base`) only exposes `step()`
returns of video/audio data and accepts controller inputs. No memory inspection
APIs are allowed or planned.

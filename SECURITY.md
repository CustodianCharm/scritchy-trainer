# Security Policy

## Supported versions
Only the latest tagged release of Scritchy Scratchy Trainer receives fixes.

## Scope
- Memory read/write offsets (`core/offsets.py`)
- Input injection via `pynput` / `keyboard`
- Overlay rendering (`handlers/overlay_handler.py`)

## Reporting
Do **not** open a public issue for memory-corruption or RCE bugs.
Email `security@scritchy-trainer.dev` with a PoC and build hash.
We'll acknowledge within 72 hours.

## Out of scope
- Bans issued by the anti-cheat after using the trainer
- Detection by third-party servers running custom AC

Use at your own risk. This is an educational project.
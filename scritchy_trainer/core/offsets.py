"""Memory offsets for Scritchy Scratchy client builds.

Update these whenever the game patches. Each entry is annotated with the
build hash it was dumped from. Educational reverse-engineering only.
"""
from typing import Optional

OFFSETS: dict[str, dict[str, int]] = {
    "1.4.2.c0ffee": {
        "player_base": 0x00A4F210,
        "combo_counter": 0x0000018C,
        "accuracy_ptr": 0x000002A0,
        "note_speed": 0x00000310,
        "hit_window_ms": 0x00000344,
    },
    "1.5.0.deadbe": {
        "player_base": 0x00A5C3A0,
        "combo_counter": 0x00000190,
        "accuracy_ptr": 0x000002A8,
        "note_speed": 0x00000318,
        "hit_window_ms": 0x0000034C,
    },
}

CURRENT_BUILD = "1.5.0.deadbe"


def resolve(name: str, build: Optional[str] = None) -> int:
    key = build or CURRENT_BUILD
    table = OFFSETS.get(key)
    if table is None:
        raise KeyError(f"unknown build: {key}")
    if name not in table:
        raise KeyError(f"offset '{name}' not present for build {key}")
    return table[name]
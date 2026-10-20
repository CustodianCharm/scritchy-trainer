from scritchy_trainer.core.offsets import resolve, OFFSETS, CURRENT_BUILD


def test_current_build_resolves():
    base = resolve("player_base")
    assert isinstance(base, int)
    assert base > 0


def test_all_offsets_positive():
    for build, table in OFFSETS.items():
        for name, value in table.items():
            assert value >= 0, f"{build}/{name} is negative"


def test_unknown_offset_raises():
    try:
        resolve("does_not_exist")
    except KeyError:
        return
    raise AssertionError("expected KeyError")
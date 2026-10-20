from scritchy_trainer.helpers.timing import ms_to_ticks, ticks_to_ms


def test_ms_to_ticks_roundtrip():
    for ms in (0, 16, 50, 90, 250):
        ticks = ms_to_ticks(ms)
        back = ticks_to_ms(ticks)
        assert abs(back - ms) < 20


def test_negative_ms_clamped():
    assert ms_to_ticks(-100) == 0
</final>
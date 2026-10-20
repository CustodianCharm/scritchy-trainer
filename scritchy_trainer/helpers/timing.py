TICK_HZ = 60


def ms_to_ticks(ms: float, hz: int = TICK_HZ) -> int:
    return max(0, int(round((ms / 1000.0) * hz)))


def ticks_to_ms(ticks: int, hz: int = TICK_HZ) -> float:
    return (ticks / hz) * 1000.0
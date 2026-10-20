"""Reads the combo counter and mirrors it to a local stat store."""
from scritchy_trainer.core.offsets import resolve


class ComboTracker:
    name = "combo_tracker"

    def __init__(self) -> None:
        self.ctx = None
        self.last_combo = 0
        self.peak = 0

    def setup(self, ctx) -> None:
        self.ctx = ctx
        self.base = resolve("player_base")
        self.combo_off = resolve("combo_counter")

    def tick(self) -> None:
        if self.ctx is None:
            return
        # read via ctx.process (stubbed in dry-run)
        combo = self._read_combo()
        if combo > self.peak:
            self.peak = combo
        self.last_combo = combo

    def _read_combo(self) -> int:
        reader = getattr(self.ctx.process, "read_int", None)
        if reader is None:
            return 0
        return reader(self.base + self.combo_off)

    def teardown(self) -> None:
        self.ctx.log.info("combo peak=%d", self.peak)
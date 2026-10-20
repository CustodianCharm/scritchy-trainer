"""Adjusts the effective hit window (timing leniency) exposed to the client."""
from scritchy_trainer.core.offsets import resolve


class HitWindowHandler:
    name = "hit_window"

    def __init__(self, target_ms: int = 90) -> None:
        self.target_ms = target_ms
        self._applied = False
        self.ctx = None

    def setup(self, ctx) -> None:
        self.ctx = ctx
        self.offset = resolve("hit_window_ms")

    def tick(self) -> None:
        if self._applied or self.ctx is None:
            return
        writer = getattr(self.ctx.process, "write_int", None)
        if writer is None:
            self.ctx.log.debug("dry-run: would set hit window to %dms", self.target_ms)
            self._applied = True
            return
        writer(self.offset, self.target_ms)
        self._applied = True
        self.ctx.log.info("hit window set to %dms", self.target_ms)

    def teardown(self) -> None:
        self._applied = False
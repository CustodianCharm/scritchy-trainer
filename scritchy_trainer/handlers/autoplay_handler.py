"""Optional autoplay: reads upcoming notes and injects key presses."""
import time
import random

from scritchy_trainer.helpers.key_sender import send_key
from scritchy_trainer.core.offsets import resolve

LANE_KEYS = ["d", "f", "j", "k"]


class AutoplayHandler:
    name = "autoplay"

    def __init__(self, jitter_ms: int = 12) -> None:
        self.jitter_ms = jitter_ms
        self.ctx = None
        self._next_note_at = 0.0

    def setup(self, ctx) -> None:
        self.ctx = ctx
        self.note_speed_off = resolve("note_speed")

    def tick(self) -> None:
        now = time.perf_counter()
        if now < self._next_note_at:
            return
        lane = random.randrange(len(LANE_KEYS))
        send_key(LANE_KEYS[lane])
        jitter = random.uniform(0.005, self.jitter_ms / 1000.0)
        self._next_note_at = now + 0.08 + jitter

    def teardown(self) -> None:
        if self.ctx:
            self.ctx.log.info("autoplay stopped")
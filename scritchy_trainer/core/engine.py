"""Central trainer engine: dispatches ticks to registered handlers."""
import logging
import time
from typing import Protocol

from scritchy_trainer.bootstrap.config_loader import TrainerConfig


class Handler(Protocol):
    name: str
    def setup(self, ctx: "EngineContext") -> None: ...
    def tick(self) -> None: ...
    def teardown(self) -> None: ...


class EngineContext:
    def __init__(self, process, config: TrainerConfig):
        self.process = process
        self.config = config
        self.log = logging.getLogger("scritchy.engine")


class TrainerEngine:
    TICK_HZ = 60

    def __init__(self, process, config: TrainerConfig):
        self.process = process
        self.config = config
        self.handlers: list[Handler] = []
        self._running = False
        self.log = logging.getLogger("scritchy.engine")

    def register(self, handler: Handler) -> None:
        self.handlers.append(handler)

    def run(self) -> None:
        ctx = EngineContext(self.process, self.config)
        for h in self.handlers:
            h.setup(ctx)
            self.log.info("handler up: %s", h.name)
        self._running = True
        period = 1.0 / self.TICK_HZ
        while self._running:
            start = time.perf_counter()
            for h in self.handlers:
                try:
                    h.tick()
                except Exception as exc:
                    self.log.exception("handler %s failed: %s", h.name, exc)
            elapsed = time.perf_counter() - start
            if elapsed < period:
                time.sleep(period - elapsed)

    def shutdown(self) -> None:
        self._running = False
        for h in reversed(self.handlers):
            try:
                h.teardown()
            except Exception:
                pass
"""Bootstrap entry point for the Scritchy Scratchy Trainer."""
import sys
import logging
from pathlib import Path

from scritchy_trainer.bootstrap.config_loader import load_config
from scritchy_trainer.core.engine import TrainerEngine
from scritchy_trainer.core.game_attach import attach_to_process
from scritchy_trainer.helpers.logger import setup_logger
from scritchy_trainer.handlers import register_default_handlers


def main() -> int:
    cfg = load_config(Path("config/default.yaml"))
    log = setup_logger(cfg.log_level)
    log.info("Scritchy Scratchy Trainer starting up")

    proc = attach_to_process(cfg.process_name)
    if proc is None:
        log.error("Could not find process: %s", cfg.process_name)
        return 1

    engine = TrainerEngine(proc, cfg)
    for handler in register_default_handlers(cfg):
        engine.register(handler)

    try:
        engine.run()
    except KeyboardInterrupt:
        log.info("Shutdown requested")
    finally:
        engine.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
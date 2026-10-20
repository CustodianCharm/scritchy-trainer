import logging
import sys
from pathlib import Path


def setup_logger(level: str = "INFO") -> logging.Logger:
    root = logging.getLogger("scritchy")
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    if root.handlers:
        return root

    fmt = logging.Formatter("[%(asctime)s] %(levelname)-7s %(name)s :: %(message)s")

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    root.addHandler(sh)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    fh = logging.FileHandler(log_dir / "scritchy-trainer.log", encoding="utf-8")
    fh.setFormatter(fmt)
    root.addHandler(fh)
    return root
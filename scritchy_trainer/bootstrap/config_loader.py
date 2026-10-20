import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class TrainerConfig:
    process_name: str = "ScritchyScratchy.exe"
    log_level: str = "INFO"
    overlay: dict = field(default_factory=dict)
    features: dict = field(default_factory=dict)
    hotkeys: dict = field(default_factory=dict)


def load_config(path: Path) -> TrainerConfig:
    if not path.exists():
        return TrainerConfig()
    with path.open("r", encoding="utf-8") as fh:
        raw: dict[str, Any] = yaml.safe_load(fh) or {}
    return TrainerConfig(
        process_name=raw.get("process_name", TrainerConfig.process_name),
        log_level=raw.get("log_level", "INFO"),
        overlay=raw.get("overlay", {}),
        features=raw.get("features", {}),
        hotkeys=raw.get("hotkeys", {}),
    )
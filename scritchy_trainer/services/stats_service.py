"""Persists session stats to a local JSON dump for the overlay."""
import json
from pathlib import Path

from scritchy_trainer.models.session import SessionStats


class StatsService:
    def __init__(self, path: Path = Path("logs/session.json")):
        self.path = path
        self.session = SessionStats()

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "peak_combo": self.session.peak_combo,
            "notes_hit": self.session.notes_hit,
            "notes_missed": self.session.notes_missed,
            "accuracy": round(self.session.accuracy, 2),
        }
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
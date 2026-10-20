from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SessionStats:
    started_at: datetime = field(default_factory=datetime.utcnow)
    peak_combo: int = 0
    notes_hit: int = 0
    notes_missed: int = 0
    accuracy: float = 0.0

    def record_hit(self, combo: int) -> None:
        self.notes_hit += 1
        if combo > self.peak_combo:
            self.peak_combo = combo
        self._recompute()

    def record_miss(self) -> None:
        self.notes_missed += 1
        self._recompute()

    def _recompute(self) -> None:
        total = self.notes_hit + self.notes_missed
        self.accuracy = (self.notes_hit / total * 100.0) if total else 0.0
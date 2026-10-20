from dataclasses import dataclass


@dataclass(slots=True)
class NoteEvent:
    lane: int
    timestamp_ms: int
    duration_ms: int = 0

    @property
    def end_ms(self) -> int:
        return self.timestamp_ms + self.duration_ms

    def is_hold(self) -> bool:
        return self.duration_ms > 0
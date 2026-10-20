"""Cross-platform-safe key injection wrapper."""
try:
    from pynput.keyboard import Controller as _KB
    _kb = _KB()
except Exception:  # pragma: no cover
    _kb = None


def send_key(key: str) -> None:
    if _kb is None:
        return
    try:
        _kb.press(key)
        _kb.release(key)
    except Exception:
        pass
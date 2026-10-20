"""Global hotkey registration for toggling features at runtime."""
try:
    import keyboard  # type: ignore
except Exception:  # pragma: no cover
    keyboard = None


class HotkeyService:
    def __init__(self) -> None:
        self._bindings: dict[str, callable] = {}

    def bind(self, combo: str, callback) -> None:
        self._bindings[combo] = callback
        if keyboard is not None:
            try:
                keyboard.add_hotkey(combo, callback)
            except Exception:
                pass

    def unbind_all(self) -> None:
        if keyboard is not None:
            try:
                keyboard.unhook_all_hotkeys()
            except Exception:
                pass
        self._bindings.clear()
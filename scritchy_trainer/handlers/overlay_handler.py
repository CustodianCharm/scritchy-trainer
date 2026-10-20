"""Lightweight HUD overlay using an always-on-top Tk window."""
import threading


class OverlayHandler:
    name = "overlay"

    def __init__(self) -> None:
        self._thread: threading.Thread | None = None
        self._stop = threading.Event()
        self.ctx = None

    def setup(self, ctx) -> None:
        self.ctx = ctx
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def tick(self) -> None:
        pass  # overlay runs on its own thread

    def _run(self) -> None:
        try:
            import tkinter as tk
        except ImportError:
            if self.ctx:
                self.ctx.log.warning("tkinter missing — overlay disabled")
            return
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.attributes("-alpha", 0.75)
        root.geometry("240x80+20+20")
        label = tk.Label(root, text="scritchy-trainer", fg="#00ff9c", bg="#101010")
        label.pack(expand=True, fill="both")
        while not self._stop.is_set():
            root.update()
        root.destroy()

    def teardown(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=1.0)
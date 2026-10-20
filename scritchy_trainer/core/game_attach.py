"""Attach to the Scritchy Scratchy process via win32."""
import logging
from typing import Optional

try:
    import win32process  # type: ignore
    import win32api  # type: ignore
except ImportError:  # non-Windows dev boxes
    win32process = None
    win32api = None

log = logging.getLogger("scritchy.attach")


class ProcessHandle:
    def __init__(self, pid: int, name: str):
        self.pid = pid
        self.name = name


def attach_to_process(name: str) -> Optional[ProcessHandle]:
    if win32process is None:
        log.warning("pywin32 unavailable — running in dry-run mode")
        return ProcessHandle(pid=0, name=name)
    try:
        for pid in win32process.EnumProcesses():
            try:
                handle = win32api.OpenProcess(0x0410, False, pid)
                exe = win32process.GetModuleFileNameEx(handle, 0)
                if exe.lower().endswith(name.lower()):
                    log.info("attached to %s (pid=%d)", name, pid)
                    return ProcessHandle(pid=pid, name=name)
            except Exception:
                continue
    except Exception as exc:
        log.error("enumeration failed: %s", exc)
    return None
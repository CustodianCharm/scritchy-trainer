from scritchy_trainer.bootstrap.config_loader import TrainerConfig
from .overlay_handler import OverlayHandler
from .hit_window_handler import HitWindowHandler
from .combo_tracker import ComboTracker
from .autoplay_handler import AutoplayHandler


def register_default_handlers(cfg: TrainerConfig):
    handlers = [ComboTracker(), HitWindowHandler()]
    if cfg.features.get("overlay", True):
        handlers.append(OverlayHandler())
    if cfg.features.get("autoplay", False):
        handlers.append(AutoplayHandler())
    return handlers
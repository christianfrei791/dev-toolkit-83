import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class AutoClickerConfig:
    """Configuration settings for the autoclicker module."""

    interval_ms: int = 100
    random_variance_ms: int = 10
    button: str = "left"
    click_type: str = "single"
    toggle_hotkey: str = "f6"
    stop_hotkey: str = "f7"
    max_clicks: int = 0

    def sanitize(self) -> None:
        """Ensure configuration values are within valid operational bounds."""
        self.interval_ms = max(1, self.interval_ms)
        self.random_variance_ms = max(0, min(self.random_variance_ms, self.interval_ms))
        if self.button not in ("left", "right", "middle"):
            self.button = "left"
        if self.click_type not in ("single", "double"):
            self.click_type = "single"
        if self.max_clicks < 0:
            self.max_clicks = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to a dictionary representation."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AutoClickerConfig":
        """Create instance from dictionary with sanitized fields."""
        valid_keys = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        cfg = cls(**filtered)
        cfg.sanitize()
        return cfg

    def save_to_file(self, path: Path) -> None:
        """Persist config to a JSON file."""
        path.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load_from_file(cls, path: Path) -> "AutoClickerConfig":
        """Load config from a JSON file, returning defaults if missing."""
        if not path.is_file():
            return cls()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return cls.from_dict(data)
        except (json.JSONDecodeError, OSError):
            return cls()

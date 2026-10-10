import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval_seconds": 0.1,
    "mouse_button": "left",
    "click_type": "single",
    "hotkey_start": "f6",
    "hotkey_stop": "f7",
    "max_clicks": 0,
    "randomize_interval": False,
    "interval_jitter": 0.02,
}


class ConfigManager:
    """Handles loading, saving, and accessing autoclicker settings."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config: Dict[str, Any] = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads config from JSON file or creates default file if missing."""
        if not os.path.exists(self.filepath):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            merged = DEFAULT_CONFIG.copy()
            merged.update(loaded)
            return merged
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save_config(self, data: Dict[str, Any] = None) -> None:
        """Saves current or provided configuration to disk."""
        to_save = data if data is not None else self.config
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(to_save, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a config value by key."""
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Updates a config value and persists changes."""
        self.config[key] = value
        self.save_config()

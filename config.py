import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval_seconds": 0.1,
    "mouse_button": "left",
    "click_type": "single",
    "start_hotkey": "f6",
    "stop_hotkey": "f7",
    "max_clicks": 0  # 0 means infinite clicks
}

class ConfigLoader:
    """Loads, validates, and saves configuration settings for the autoclicker."""

    def __init__(self, filepath: str = "autoclicker_config.json"):
        self.filepath = filepath
        self.config = self.load()

    def load(self) -> Dict[str, Any]:
        """Loads config from file, merging with defaults to handle missing keys."""
        if not os.path.exists(self.filepath):
            self.save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
                
            # Merge defaults with loaded data to ensure schema completeness
            merged_config = DEFAULT_CONFIG.copy()
            if isinstance(loaded_data, dict):
                for key, value in loaded_data.items():
                    if key in DEFAULT_CONFIG:
                        # Basic type safety check
                        if isinstance(value, type(DEFAULT_CONFIG[key])):
                            merged_config[key] = value
            return merged_config
        except (json.JSONDecodeError, IOError):
            # Return default config if file is corrupted or unreadable
            return DEFAULT_CONFIG.copy()

    def save(self, data: Dict[str, Any]) -> bool:
        """Saves the provided configuration dictionary to the file path."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            self.config = data
            return True
        except IOError:
            return False

    def get(self, key: str) -> Any:
        """Retrieves a config value, falling back to defaults if missing."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))

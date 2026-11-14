import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": True,
    "hotkey": "f6"
}

def load_configuration(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file or returns defaults if missing.
    """
    if not os.path.exists(filepath):
        save_configuration(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as file:
            config = json.load(file)
            # Ensure defaults for missing keys
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_configuration(filepath: str, config: Dict[str, Any]) -> None:
    """
    Persists the current configuration dictionary to disk.
    """
    try:
        with open(filepath, "w") as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")
import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> dict:
    """Loads configuration from disk or returns defaults if missing."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure missing keys are handled
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: dict, filepath: str = "config.json") -> None:
    """Persists configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")
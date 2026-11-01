import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "hotkey": "f6",
    "button": "left",
    "repeat": True
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(config: Dict[str, Any], path: str = "config.json") -> None:
    """
    Persists configuration dictionary to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(config, f, indent=4)
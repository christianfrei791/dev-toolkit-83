import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hold_time": 0.05,
    "repeat": -1
}

CONFIG_PATH = "config.json"

def load_config() -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_PATH, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure missing keys are handled
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any]) -> None:
    """Saves provided dictionary to config file."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    current_config = load_config()
    print(f"Loaded configuration: {current_config}")
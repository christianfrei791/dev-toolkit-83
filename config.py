import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": 0
}

def load_config(filepath="settings.json"):
    """Loads user settings from local json file."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (IOError, json.JSONDecodeError):
        return DEFAULT_CONFIG

def save_config(config, filepath="settings.json"):
    """Persists current configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Configuration save failed: {e}")
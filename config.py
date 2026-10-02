import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "repeat_count": 0,
    "hotkey": "f6"
}

def load_config(filepath="config.json"):
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge defaults with user settings
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config_dict, filepath="config.json"):
    """Persists current configuration to JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config_dict, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

if __name__ == "__main__":
    current_cfg = load_config()
    print(f"Active configuration: {current_cfg}")
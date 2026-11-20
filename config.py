import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "max_clicks": 0,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from disk or return default settings."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {filepath}, using defaults: {e}")
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persist the current configuration to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save configuration: {e}")
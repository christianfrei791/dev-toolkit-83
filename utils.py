import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "cps": 10,
    "hotkey": "F6",
    "button": "left",
    "hold_time": 0.05
}

def load_autoclicker_config(filepath: str) -> Dict[str, Any]:
    """Load configuration from JSON file or return defaults."""
    if not os.path.exists(filepath):
        save_autoclicker_config(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            # Merge with defaults to ensure all keys exist
            config = DEFAULT_CONFIG.copy()
            config.update(data)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_autoclicker_config(filepath: str, config: Dict[str, Any]) -> bool:
    """Save configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def calculate_delay(cps: float) -> float:
    """Calculate sleep delay in seconds based on clicks per second."""
    if cps <= 0:
        return 1.0
    return 1.0 / float(cps)

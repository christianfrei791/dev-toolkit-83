import json
import os
from typing import Dict, Any

CONFIG_PATH = "settings.json"

def load_click_settings() -> Dict[str, Any]:
    """Reads autoclicker configuration from local storage."""
    if not os.path.exists(CONFIG_PATH):
        return {"interval": 0.1, "button": "left", "repeat": -1}
    
    with open(CONFIG_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_settings(data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to local storage."""
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures click coordinates are within bounds."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def format_click_stats(clicks: int, duration: float) -> str:
    """Generates human readable performance summary strings."""
    cps = clicks / duration if duration > 0 else 0
    return f"Total clicks: {clicks} | Average CPS: {cps:.2f}"
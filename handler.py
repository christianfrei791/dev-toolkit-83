import json
import os
from typing import Dict, Any

def load_clicker_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker parameters from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 1}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_clicker_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to disk safely."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_params(data: Dict[str, Any]) -> bool:
    """Checks validity of click rate and count."""
    interval = data.get("interval", 0)
    repeats = data.get("repeats", 0)
    return isinstance(interval, (int, float)) and interval > 0 and isinstance(repeats, int)

def sanitize_coords(coords: tuple) -> tuple:
    """Ensures coordinates stay within non-negative bounds."""
    return (max(0, coords[0]), max(0, coords[1]))
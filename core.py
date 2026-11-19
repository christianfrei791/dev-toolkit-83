import json
import os
from typing import Dict, Any

def load_click_profile(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 1}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to JSON storage."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def validate_profile(data: Dict[str, Any]) -> bool:
    """Ensures configuration keys meet functional requirements."""
    required_keys = {"interval", "button", "repeats"}
    return all(key in data for key in required_keys) and isinstance(data["interval"], (int, float))
import json
import os
from typing import Dict, Any

def load_click_profile(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "clicks": 100, "button": "left"}
    
    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Saves current click settings to persistent storage."""
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Ensures configuration values are within safe bounds."""
    interval = data.get("interval", 0.1)
    clicks = data.get("clicks", 1)
    
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False
    if not isinstance(clicks, int) or clicks < 0:
        return False
    return True
import json
import os
from typing import Dict, Any

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "clicks": 100, "button": "left"}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def validate_interval(interval: float) -> float:
    """Ensures click interval is within safe bounds."""
    return max(0.01, min(interval, 60.0))

def format_click_stats(count: int, duration: float) -> str:
    """Returns string representation of session performance."""
    cps = count / duration if duration > 0 else 0
    return f"Performed {count} clicks at {cps:.2f} CPS"
import json
import os
from typing import Dict, Any

def load_clicker_profile(filepath: str) -> Dict[str, Any]:
    """Load autoclicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "clicks": 0}

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"interval": 0.1, "button": "left", "clicks": 0}

def save_clicker_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persist autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(value: float) -> float:
    """Ensure interval is within safe operating range."""
    return max(0.01, min(value, 60.0))

def format_click_stats(count: int, duration: float) -> str:
    """Convert performance metrics into readable strings."""
    cps = count / duration if duration > 0 else 0
    return f"Total: {count} | Avg: {cps:.2f} clicks/sec"
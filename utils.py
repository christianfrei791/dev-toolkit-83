import json
import os
from typing import Dict, Any

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 0}
    
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
    except IOError:
        return False

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures click coordinates are within bounds."""
    return x >= 0 and y >= 0

def format_click_stats(clicks: int, duration: float) -> str:
    """Calculates and formats performance metrics."""
    rate = clicks / duration if duration > 0 else 0
    return f"Total Clicks: {clicks} | Rate: {rate:.2f} clicks/sec"
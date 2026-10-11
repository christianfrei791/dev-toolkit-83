import json
import os
from typing import Any, Dict, Optional

def load_click_profile(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Ensures click delay and interval are valid numbers."""
    required = ['delay', 'interval', 'button']
    if not all(k in data for k in required):
        return False
    
    return all(isinstance(data[k], (int, float)) for k in ['delay', 'interval'])

def format_click_metrics(clicks: int, duration: float) -> str:
    """Calculates and formats clicks per second metric."""
    if duration <= 0:
        return "0.00 cps"
    cps = clicks / duration
    return f"{cps:.2f} cps"
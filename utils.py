import json
from typing import Dict, List, Any


def validate_click_config(config: Dict[str, Any]) -> bool:
    """Validates the basic configuration structure for an autoclicker session."""
    required_keys = {"interval", "button", "click_type"}
    if not required_keys.issubset(config.keys()):
        return False

    if not isinstance(config["interval"], (int, float)) or config["interval"] <= 0:
        return False

    if config["button"] not in ("left", "right", "middle"):
        return False

    if config["click_type"] not in ("single", "double", "hold"):
        return False

    return True


def parse_click_sequence(data_json: str) -> List[Dict[str, Any]]:
    """Parses a JSON string into a structured list of click events."""
    try:
        raw_events = json.loads(data_json)
        if not isinstance(raw_events, list):
            return []

        valid_events = []
        for event in raw_events:
            if isinstance(event, dict) and "x" in event and "y" in event:
                valid_events.append({
                    "x": int(event["x"]),
                    "y": int(event["y"]),
                    "delay": float(event.get("delay", 0.1)),
                    "button": str(event.get("button", "left"))
                })
        return valid_events
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def calculate_cps(interval: float) -> float:
    """Calculates clicks per second (CPS) based on interval in seconds."""
    if interval <= 0:
        return 0.0
    return round(1.0 / interval, 2)

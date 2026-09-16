import json
from typing import Any, Dict, List


def validate_click_action(action: Dict[str, Any]) -> bool:
    """Validates a single autoclicker action configuration.

    An action must contain a 'button' (left/right/middle), a positive 'interval' 
    value, and optionally, both 'x' and 'y' integer coordinates.
    """
    required_keys = {"button", "interval"}
    if not required_keys.issubset(action.keys()):
        return False

    if action["button"] not in {"left", "right", "middle"}:
        return False

    try:
        interval = float(action["interval"])
        if interval < 0.0:
            return False
    except (ValueError, TypeError):
        return False

    has_x = "x" in action and action["x"] is not None
    has_y = "y" in action and action["y"] is not None
    if has_x != has_y:
        return False

    if has_x:
        try:
            int(action["x"])
            int(action["y"])
        except (ValueError, TypeError):
            return False

    return True


def load_autoclick_profile(file_path: str) -> List[Dict[str, Any]]:
    """Loads, parses, and validates autoclicker actions from a JSON profile file.

    Returns a list of standardized actions. Returns an empty list if the file is
    missing, corrupted, or contains no valid actions.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        validated_sequence = []
        for item in data:
            if isinstance(item, dict) and validate_click_action(item):
                # Standardize schema
                validated_sequence.append(
                    {
                        "button": str(item["button"]),
                        "interval": float(item["interval"]),
                        "x": int(item["x"]) if item.get("x") is not None else None,
                        "y": int(item["y"]) if item.get("y") is not None else None,
                        "double_click": bool(item.get("double_click", False)),
                    }
                )
        return validated_sequence
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return []

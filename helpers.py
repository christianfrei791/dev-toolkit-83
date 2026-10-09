import json
import os
from typing import List, Dict, Any

def validate_click_action(action: Dict[str, Any]) -> bool:
    """Validates that a single click action has all required and valid keys."""
    required_keys = {"x", "y", "button", "delay"}
    if not required_keys.issubset(action.keys()):
        return False
    
    if not isinstance(action["x"], int) or action["x"] < 0:
        return False
    if not isinstance(action["y"], int) or action["y"] < 0:
        return False
    if action["button"] not in {"left", "right", "middle"}:
        return False
    if not isinstance(action["delay"], (int, float)) or action["delay"] < 0:
        return False
    
    return True

def save_click_sequence(filepath: str, sequence: List[Dict[str, Any]]) -> bool:
    """Saves a validated click sequence to a JSON file."""
    for action in sequence:
        if not validate_click_action(action):
            raise ValueError(f"Invalid click action found in sequence: {action}")
    
    try:
        with open(filepath, 'w') as f:
            json.dump(sequence, f, indent=4)
        return True
    except IOError:
        return False

def load_click_sequence(filepath: str) -> List[Dict[str, Any]]:
    """Loads and validates a click sequence from a JSON file."""
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r') as f:
            sequence = json.load(f)
        
        if not isinstance(sequence, list):
            raise ValueError("Click sequence must be a JSON list.")
        
        for action in sequence:
            if not validate_click_action(action):
                raise ValueError(f"Loaded file contains invalid action: {action}")
        
        return sequence
    except (json.JSONDecodeError, IOError):
        return []

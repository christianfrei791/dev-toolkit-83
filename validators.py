import re
from typing import Dict, Any, Optional

def validate_click_config(config: Dict[str, Any]) -> bool:
    """Validates autoclicker configuration parameters for range safety."""
    required_keys = {"interval", "clicks", "button"}
    if not all(k in config for k in required_keys):
        return False

    if not isinstance(config["interval"], (int, float)) or config["interval"] < 0.01:
        return False

    if not isinstance(config["clicks"], int) or config["clicks"] < -1:
        return False

    if config["button"] not in ["left", "right", "middle"]:
        return False

    return True

def sanitize_hotkey_string(hotkey: str) -> Optional[str]:
    """Cleans and validates user-provided hotkey strings."""
    if not isinstance(hotkey, str):
        return None

    clean_key = hotkey.strip().lower()
    if re.match(r"^[a-z0-9+]{1,15}$", clean_key):
        return clean_key
    
    return None

def check_coordinate_bounds(x: int, y: int, screen_size: tuple) -> bool:
    """Verifies mouse coordinates are within current display bounds."""
    width, height = screen_size
    return 0 <= x <= width and 0 <= y <= height
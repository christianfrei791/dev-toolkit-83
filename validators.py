import re
from typing import Dict, Tuple, Optional, Any

def validate_interval(interval: float) -> bool:
    """Check if click interval is valid."""
    if not isinstance(interval, (int, float)):
        return False
    return 0.01 <= interval <= 3600.0

def validate_repetitions(reps: int) -> bool:
    """Validate number of repetitions."""
    if not isinstance(reps, int):
        return False
    return 1 <= reps <= 100000

def validate_coordinates(x: int, y: int, max_x: int = 1920, max_y: int = 1080) -> bool:
    """Validate click coordinates within screen bounds."""
    if not (isinstance(x, int) and isinstance(y, int)):
        return False
    if not (isinstance(max_x, int) and isinstance(max_y, int)):
        return False
    return 0 <= x <= max_x and 0 <= y <= max_y

def validate_hotkey(hotkey: str) -> bool:
    """Validate hotkey format like ctrl+shift+a."""
    if not isinstance(hotkey, str) or not hotkey:
        return False
    parts = hotkey.lower().split('+')
    if len(parts) > 4:
        return False
    for part in parts:
        if not part.isalnum() or len(part) > 10:
            return False
    return True

def validate_button(button: str) -> bool:
    """Validate mouse button."""
    if not isinstance(button, str):
        return False
    return button.lower() in {'left', 'right', 'middle'}

class AutoclickerValidator:
    """Validator for autoclicker settings."""
    def __init__(self, screen_width: int = 1920, screen_height: int = 1080):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def validate(self, settings: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """Validate all settings and return status with message."""
        if not isinstance(settings, dict):
            return False, "Settings must be a dictionary"
        required_keys = ['interval', 'repetitions', 'x', 'y', 'hotkey', 'button']
        for key in required_keys:
            if key not in settings:
                return False, f"Missing key: {key}"
        if not validate_interval(settings['interval']):
            return False, "Invalid interval value"
        if not validate_repetitions(settings['repetitions']):
            return False, "Invalid repetitions count"
        if not validate_coordinates(
            settings['x'], settings['y'], self.screen_width, self.screen_height
        ):
            return False, "Coordinates out of bounds"
        if not validate_hotkey(settings['hotkey']):
            return False, "Invalid hotkey format"
        if not validate_button(settings['button']):
            return False, "Invalid button"
        return True, None
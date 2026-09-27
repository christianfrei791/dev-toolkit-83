import re

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures mouse coordinates are within non-negative bounds."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    """Checks if click interval is within safe operational limits."""
    return isinstance(interval, (int, float)) and 0.01 <= interval <= 60.0

def validate_hotkey(key: str) -> bool:
    """Verifies hotkey format for input listener compatibility."""
    pattern = re.compile(r'^[a-zA-Z0-9]{1}$|^f[1-9]$|^f1[0-2]$')
    return bool(pattern.match(key.lower()))

def validate_click_count(count: int) -> bool:
    """Validates click iterations are either infinite (-1) or positive."""
    return isinstance(count, int) and (count > 0 or count == -1)

def sanitize_input(user_input: str) -> str:
    """Trims whitespace and normalizes case for internal processing."""
    return str(user_input).strip().lower()
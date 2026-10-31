import re

def validate_interval(interval: float) -> bool:
    """Ensures click interval is within safe hardware limits."""
    return 0.01 <= interval <= 60.0

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates fall within standard display bounds."""
    return x >= 0 and y >= 0

def validate_hotkey(key: str) -> bool:
    """Verifies hotkey format against simple character constraints."""
    return bool(re.match(r'^[a-z0-9]$', key.lower()))

def sanitize_input(user_input: str) -> str:
    """Strips whitespace and converts to lowercase for consistency."""
    return str(user_input).strip().lower()
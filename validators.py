import logging

def validate_click_settings(interval, duration):
    """Ensures input values meet functional constraints."""
    try:
        if not isinstance(interval, (int, float)) or interval < 0.01:
            raise ValueError(f"Invalid interval: {interval}. Must be >= 0.01")
            
        if not isinstance(duration, (int, float)) or duration < 0:
            raise ValueError(f"Invalid duration: {duration}. Must be non-negative")
            
        return True
    except ValueError as e:
        logging.error(f"Validation failed: {e}")
        return False

def sanitize_input(user_input):
    """Cleans raw string input for processing."""
    if isinstance(user_input, str):
        return user_input.strip()
    return user_input

def check_bounds(x, y, max_w, max_h):
    """Verifies coordinates are within screen dimensions."""
    if 0 <= x <= max_w and 0 <= y <= max_h:
        return True
    logging.warning(f"Coordinates ({x}, {y}) out of screen bounds")
    return False
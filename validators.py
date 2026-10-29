import logging

# Configuration constraints for the autoclicker
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0
ALLOWED_BUTTONS = ['left', 'right', 'middle']

def validate_click_params(interval, button):
    """Ensures click parameters are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or not (MIN_INTERVAL <= interval <= MAX_INTERVAL):
        logging.error(f"Invalid interval: {interval}. Must be between {MIN_INTERVAL} and {MAX_INTERVAL}")
        return False

    if button not in ALLOWED_BUTTONS:
        logging.error(f"Invalid mouse button: {button}. Must be one of {ALLOWED_BUTTONS}")
        return False

    return True

def validate_coordinates(x, y):
    """Checks if provided screen coordinates are non-negative."""
    if x < 0 or y < 0:
        logging.error(f"Invalid coordinates: ({x}, {y}). Coordinates cannot be negative.")
        return False
    return True
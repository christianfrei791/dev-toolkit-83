import logging

logger = logging.getLogger(__name__)

def validate_click_params(interval: float, duration: int) -> bool:
    """Validates input parameters for the autoclicker loop."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logger.error(f"Invalid interval: {interval}. Must be >= 0.01.")
        return False

    if not isinstance(duration, int) or duration < 0:
        logger.error(f"Invalid duration: {duration}. Must be a positive integer.")
        return False

    return True

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if coordinates fall within display bounds."""
    if 0 <= x <= screen_width and 0 <= y <= screen_height:
        return True
    
    logger.warning(f"Coordinates ({x}, {y}) out of screen bounds.")
    return False

def sanitize_input(user_input: str) -> float:
    """Attempts to convert raw input to a float safely."""
    try:
        value = float(user_input)
        return max(0.01, value)
    except (ValueError, TypeError):
        logger.error(f"Input conversion failed for value: {user_input}")
        return 0.1
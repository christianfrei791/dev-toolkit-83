import logging

def validate_click_params(interval: float, duration: float) -> bool:
    """
    Validates input parameters for the autoclicker logic.
    Ensures timing constraints are within logical bounds.
    """
    logger = logging.getLogger(__name__)

    if not isinstance(interval, (int, float)) or not isinstance(duration, (int, float)):
        logger.error("Invalid parameter type: inputs must be numeric")
        return False

    if interval < 0.01:
        logger.warning("Interval too low, clamping to 0.01s")
        return False

    if duration < 0:
        logger.error("Duration cannot be negative")
        return False

    return True

def sanitize_coordinates(x: int, y: int, screen_res: tuple) -> bool:
    """
    Checks if coordinates are within defined screen resolution.
    """
    width, height = screen_res
    if 0 <= x <= width and 0 <= y <= height:
        return True
    
    logging.error(f"Coordinates ({x}, {y}) out of screen bounds")
    return False
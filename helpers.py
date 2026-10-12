import logging
from typing import Tuple, Optional, Union

logger = logging.getLogger(__name__)

class ClickCoordinateError(ValueError):
    """Raised when target click coordinates are invalid."""
    pass

class IntervalOutOfBoundsError(ValueError):
    """Raised when click interval is set below safety limits."""
    pass

def validate_screen_bounds(
    x: int, 
    y: int, 
    screen_width: int, 
    screen_height: int
) -> Tuple[int, int]:
    """Validate coordinates and clamp within active screen dimensions."""
    if screen_width <= 0 or screen_height <= 0:
        raise ClickCoordinateError("Screen dimensions must be positive integers")

    # Clamp x and y to prevent off-screen pointer exceptions
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))

    if (clamped_x, clamped_y) != (x, y):
        logger.warning(f"Coordinates ({x}, {y}) out of bounds. Clamped to ({clamped_x}, {clamped_y}).")

    return clamped_x, clamped_y

def sanitize_click_interval(interval: Union[int, float], min_limit: float = 0.001) -> float:
    """Safely parse interval to prevent CPU lockup or thread starvation."""
    try:
        val = float(interval)
    except (TypeError, ValueError) as err:
        raise IntervalOutOfBoundsError(f"Invalid click interval type/value: {interval}") from err

    if val < min_limit:
        logger.warning(f"Interval {val}s below minimum safe limit ({min_limit}s). Auto-adjusted.")
        return min_limit
    return val

def safe_parse_hotkey(hotkey_str: str) -> Optional[str]:
    """Sanitize hotkey strings to handle malformed user configurations."""
    if not hotkey_str or not isinstance(hotkey_str, str):
        return None
    
    cleaned = hotkey_str.strip().lower()
    if len(cleaned) > 25:
        logger.error("Hotkey string exceeds maximum allowable length.")
        return None
        
    return cleaned

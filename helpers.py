import logging
import pyautogui
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

def get_safe_coordinates(x: int, y: int) -> Optional[Tuple[int, int]]:
    """Validates coordinates against screen dimensions."""
    try:
        screen_width, screen_height = pyautogui.size()
        if 0 <= x < screen_width and 0 <= y < screen_height:
            return (x, y)
        logger.warning(f"Coordinates ({x}, {y}) out of bounds.")
        return None
    except pyautogui.FailSafeException as e:
        logger.error(f"Critical fail-safe triggered: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error validating screen geometry: {e}")
        return None

def execute_safe_click(x: int, y: int, interval: float = 0.1) -> bool:
    """Wraps pyautogui click with boundary and error checks."""
    coords = get_safe_coordinates(x, y)
    if not coords:
        return False

    try:
        pyautogui.click(x=coords[0], y=coords[1])
        return True
    except pyautogui.ImageNotFoundException:
        logger.error("Click target element not located on screen.")
    except Exception as e:
        logger.error(f"Execution failure during click event: {e}")
    return False
import logging
import pyautogui
import time

logger = logging.getLogger(__name__)

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with bounds checking and failure handling."""
    try:
        screen_width, screen_height = pyautogui.size()

        if not (0 <= x < screen_width and 0 <= y < screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds.")

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)

    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: mouse moved to corner.")
        raise
    except ValueError as e:
        logger.error(f"Invalid click coordinates: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error during click execution: {e}")

def batch_click(points: list):
    """Executes a series of clicks with basic validation."""
    if not isinstance(points, list):
        logger.error("Point data must be a list.")
        return

    for point in points:
        if len(point) != 2:
            logger.warning(f"Skipping invalid point format: {point}")
            continue
        safe_click(point[0], point[1])
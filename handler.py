import logging
import pyautogui

logger = logging.getLogger(__name__)

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with screen boundary and input validation."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
            
        pyautogui.click(x, y)
        logger.debug(f"Successfully clicked at {x}, {y}")
        
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: mouse moved to corner")
        raise
    except ValueError as ve:
        logger.error(f"Invalid input parameters: {ve}")
    except Exception as e:
        logger.error(f"Unexpected error during click execution: {e}")

def execute_sequence(sequence: list):
    """Processes a list of coordinate tuples with error isolation."""
    if not isinstance(sequence, list):
        logger.error("Invalid sequence format: expected list")
        return

    for step in sequence:
        try:
            x, y = step
            safe_click(x, y)
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping malformed coordinate point {step}: {e}")
            continue
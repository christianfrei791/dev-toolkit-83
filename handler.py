import logging
import pyautogui
import time

# Configure logger for dev-toolkit-83
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-83')

def safe_click(x, y, interval=0.1):
    """Performs a mouse click with robust error boundary checks."""
    try:
        # Validate coordinates against screen resolution
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)

    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: process aborted by user")
        raise
    except ValueError as e:
        logger.error(f"Invalid input parameters: {e}")
    except Exception as e:
        logger.error(f"Unexpected automation failure: {type(e).__name__} - {e}")

def run_click_sequence(coords_list):
    """Iterates through sequence with error recovery logic."""
    for i, (x, y) in enumerate(coords_list):
        try:
            safe_click(x, y)
        except (TypeError, ValueError):
            logger.warning(f"Skipping invalid coordinate at index {i}")
            continue
        except Exception:
            logger.error("Critical runtime error during sequence execution")
            break
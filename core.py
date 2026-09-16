import pyautogui
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-83')

def execute_click(x, y, interval=0.1):
    """Performs a safe click operation with boundary validation."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) outside screen bounds.")
        
        pyautogui.click(x, y)
        time.sleep(max(0, interval))
        
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered by user. Aborting.")
        raise
    except ValueError as e:
        logger.warning(f"Validation error: {e}")
    except Exception as e:
        logger.critical(f"Unexpected click failure: {e}")

def run_sequence(clicks):
    """Iterates through click list with recovery logic."""
    for point in clicks:
        try:
            execute_click(point.get('x', 0), point.get('y', 0))
        except (TypeError, AttributeError):
            logger.error("Invalid data structure in click sequence")
            continue
        except Exception:
            break
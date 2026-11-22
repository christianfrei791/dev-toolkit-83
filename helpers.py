import pyautogui
import time
import random
from typing import Tuple

def get_random_delay(min_ms: int, max_ms: int) -> float:
    """Calculates random delay in seconds between click events."""
    return random.randint(min_ms, max_ms) / 1000.0

def perform_safe_click(x: int, y: int, jitter: int = 0) -> None:
    """Performs a click with optional pixel jitter for stealth."""
    target_x = x + random.randint(-jitter, jitter)
    target_y = y + random.randint(-jitter, jitter)
    pyautogui.click(target_x, target_y)

def wait_for_sequence(duration: float) -> None:
    """Blocking sleep for controlled operation pacing."""
    time.sleep(duration)

def get_mouse_position() -> Tuple[int, int]:
    """Returns current (x, y) coordinates of the cursor."""
    return pyautogui.position()

def safe_emergency_stop(key: str = 'q') -> bool:
    """Checks if emergency stop key is pressed."""
    try:
        return pyautogui.press(key, _pause=False) is None # Placeholder for hotkey logic
    except Exception:
        return False
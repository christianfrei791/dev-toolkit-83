import time
import pyautogui
import random
from typing import Tuple

def safe_click(x: int, y: int) -> None:
    """Performs a mouse click with a small random offset."""
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    pyautogui.click(x + offset_x, y + offset_y)

def human_delay(min_sec: float = 0.1, max_sec: float = 0.5) -> None:
    """Sleeps for a random duration to mimic human interaction."""
    time.sleep(random.uniform(min_sec, max_sec))

def get_screen_center() -> Tuple[int, int]:
    """Returns the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return (width // 2, height // 2)

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are within screen boundaries."""
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height

def emergency_stop() -> None:
    """Forces a mouse move to corner to trigger failsafe."""
    pyautogui.moveTo(0, 0)
    raise InterruptedError("Emergency stop triggered by user")
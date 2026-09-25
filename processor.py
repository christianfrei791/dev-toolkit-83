import pyautogui
import time
import random
from typing import Tuple

def move_and_click(x: int, y: int, duration: float = 0.1) -> None:
    """Move mouse to coordinates and perform a click."""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def randomized_delay(min_sec: float, max_sec: float) -> None:
    """Pause execution for a random duration to mimic human behavior."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def get_screen_center() -> Tuple[int, int]:
    """Calculate the center point of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def perform_drag(start: Tuple[int, int], end: Tuple[int, int], speed: float = 0.5) -> None:
    """Execute a drag operation between two points."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=speed)

def safety_check(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Validate if the target coordinates are within screen bounds."""
    return 0 <= x <= screen_width and 0 <= y <= screen_height
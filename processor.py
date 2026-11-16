import time
import random
import pyautogui

def execute_click(x: int, y: int, interval: float = 0.0) -> None:
    """Performs a mouse click at specified screen coordinates."""
    pyautogui.click(x=x, y=y)
    if interval > 0:
        time.sleep(interval)

def perform_jitter_click(x: int, y: int, radius: int = 5) -> None:
    """Performs a click with slight spatial randomization."""
    target_x = x + random.randint(-radius, radius)
    target_y = y + random.randint(-radius, radius)
    pyautogui.click(x=target_x, y=target_y)

def wait_random(min_s: float, max_s: float) -> None:
    """Pauses execution for a random duration to mimic human behavior."""
    delay = random.uniform(min_s, max_s)
    time.sleep(delay)

def get_screen_center() -> tuple:
    """Calculates the center of the primary display."""
    width, height = pyautogui.size()
    return (width // 2, height // 2)

def drag_and_drop(start: tuple, end: tuple, duration: float = 0.5) -> None:
    """Simulates a drag movement between two points."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=duration, button='left')

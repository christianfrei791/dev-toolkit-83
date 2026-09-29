import time
import pyautogui
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with a small random jitter to avoid detection."""
    jitter_x = random.randint(-2, 2)
    jitter_y = random.randint(-2, 2)
    pyautogui.click(x + jitter_x, y + jitter_y)
    time.sleep(interval)

def human_delay(min_ms: int = 50, max_ms: int = 200):
    """Injects random sleep to simulate human input patterns."""
    delay = random.uniform(min_ms / 1000.0, max_ms / 1000.0)
    time.sleep(delay)

def get_screen_center():
    """Calculates coordinates for the center of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def validate_bounds(x: int, y: int):
    """Ensures click coordinates are within screen dimensions."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height
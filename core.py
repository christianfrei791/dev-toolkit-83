import pyautogui
import time
import random

def safe_click(x, y, interval=0.1):
    """Performs a mouse click with random jitter to avoid detection."""
    jitter_x = random.randint(-2, 2)
    jitter_y = random.randint(-2, 2)
    pyautogui.click(x + jitter_x, y + jitter_y)
    time.sleep(interval)

def perform_sequence(coords, delay=1.0):
    """Iterates through a list of coordinate tuples and clicks them."""
    for x, y in coords:
        safe_click(x, y)
        time.sleep(delay)

def smart_wait(min_sec, max_sec):
    """Pauses execution for a randomized duration."""
    duration = random.uniform(min_sec, max_sec)
    time.sleep(duration)

def screen_resolution_check():
    """Validates screen boundaries for click safety."""
    return pyautogui.size()

def emergency_stop():
    """Force quit logic triggered by mouse movement to corner."""
    pyautogui.FAILSAFE = True
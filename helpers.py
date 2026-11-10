import time
import random
import pyautogui

def safe_click(x, y, interval=0.1):
    """Performs a mouse click at coordinates with a small random jitter."""
    jitter_x = random.randint(-2, 2)
    jitter_y = random.randint(-2, 2)
    pyautogui.click(x + jitter_x, y + jitter_y)
    time.sleep(interval)

def hold_key(key, duration):
    """Holds a keyboard key for a specified duration."""
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def wait_random(min_s, max_s):
    """Sleeps for a random interval within given range."""
    delay = random.uniform(min_s, max_s)
    time.sleep(delay)

def get_screen_center():
    """Returns the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def is_pixel_color(x, y, color):
    """Checks if a pixel matches the provided RGB tuple."""
    return pyautogui.pixelMatchesColor(x, y, color)

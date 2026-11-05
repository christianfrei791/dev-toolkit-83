import time
import pyautogui
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Move mouse to coordinates and perform a click with jitter."""
    target_x = x + random.randint(-2, 2)
    target_y = y + random.randint(-2, 2)
    pyautogui.moveTo(target_x, target_y, duration=0.2)
    pyautogui.click()
    time.sleep(interval)

def get_screen_center():
    """Calculate the center point of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def sleep_random(min_s: float, max_s: float):
    """Wait for a randomized duration to simulate human behavior."""
    delay = random.uniform(min_s, max_s)
    time.sleep(delay)

def validate_coordinates(x: int, y: int):
    """Check if coordinates are within screen bounds."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height

def perform_sequence(points: list):
    """Iterate through a list of (x, y) tuples and click them."""
    for x, y in points:
        if validate_coordinates(x, y):
            safe_click(x, y)
        else:
            print(f"Invalid coordinates: {x}, {y}")
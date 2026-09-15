import pyautogui
import time
import random

def safe_click(x, y, interval=(0.1, 0.3)):
    """Performs a click with randomized delay to mimic human behavior."""
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(*interval))
    pyautogui.click()

def drag_to(start_x, start_y, end_x, end_y, duration=0.5):
    """Executes a smooth drag operation between two coordinates."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, tween=pyautogui.easeInOutQuad)

def click_sequence(coordinates, delay=0.5):
    """Iterates through a list of (x, y) tuples and clicks each."""
    for x, y in coordinates:
        safe_click(x, y)
        time.sleep(delay)

def get_screen_bounds():
    """Returns the dimensions of the primary display."""
    width, height = pyautogui.size()
    return {'width': width, 'height': height}

def validate_position(x, y):
    """Checks if coordinates are within the current screen resolution."""
    bounds = get_screen_bounds()
    return 0 <= x <= bounds['width'] and 0 <= y <= bounds['height']
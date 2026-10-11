import time
import pyautogui
import logging

def click_at(x, y, interval=0.1):
    """Perform mouse click at specific coordinates with delay."""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def get_screen_center():
    """Calculate center of the primary monitor."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def safe_execute(func, *args, **kwargs):
    """Execute function with basic error trapping."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logging.error(f"Execution error in {func.__name__}: {e}")
        return None

def validate_coordinates(x, y):
    """Ensure coordinates are within screen bounds."""
    width, height = pyautogui.size()
    if 0 <= x <= width and 0 <= y <= height:
        return True
    return False

def perform_sequence(coords_list, delay=0.5):
    """Execute a list of clicks sequentially."""
    for x, y in coords_list:
        if validate_coordinates(x, y):
            click_at(x, y)
            time.sleep(delay)
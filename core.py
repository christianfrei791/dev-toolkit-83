import time
import pyautogui
import random

def safe_click(x, y, delay_range=(0.1, 0.5)):
    """Performs a click at coordinates with randomized delay."""
    time.sleep(random.uniform(*delay_range))
    pyautogui.click(x, y)

def smart_drag(start_pos, end_pos, duration=0.5):
    """Drags mouse between points with linear easing."""
    pyautogui.moveTo(*start_pos)
    pyautogui.dragTo(*end_pos, duration=duration, button='left')

def get_screen_center():
    """Calculates the center of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def confirm_coords(x, y):
    """Validates that coordinates are within screen bounds."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height

def perform_sequence(actions):
    """Executes a list of actions with configurable timing."""
    for action in actions:
        func, args = action
        func(*args)
        time.sleep(0.1)
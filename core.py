import pyautogui
import time
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Move mouse to coordinates and perform a click with safety delays."""
    pyautogui.moveTo(x, y, duration=0.2)
    time.sleep(interval)
    pyautogui.click()

def randomized_click(x: int, y: int, variance: int = 5):
    """Perform click at slightly offset coordinates to simulate human behavior."""
    target_x = x + random.randint(-variance, variance)
    target_y = y + random.randint(-variance, variance)
    safe_click(target_x, target_y)

def hold_key(key: str, duration: float):
    """Hold down a specific keyboard key for a set amount of time."""
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def get_screen_center():
    """Retrieve the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def emergency_stop():
    """Fail-safe trigger to halt automation immediately."""
    pyautogui.FAILSAFE = True
    print("Emergency stop enabled: move mouse to corner to abort")
import time
import pyautogui
from typing import Tuple, Optional

class ClickHandler:
    """Handles mouse interaction events for the autoclicker."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initializes the click handler with a defined interval."""
        self.interval: float = interval

    def perform_click(self, coordinates: Optional[Tuple[int, int]] = None) -> None:
        """
        Executes a mouse click at specific coordinates or current location.
        
        :param coordinates: Tuple of (x, y) pixels
        """
        if coordinates:
            pyautogui.click(x=coordinates[0], y=coordinates[1])
        else:
            pyautogui.click()

    def run_sequence(self, iterations: int, coords: Optional[Tuple[int, int]] = None) -> None:
        """
        Executes a loop of clicks with a set delay.
        
        :param iterations: Number of times to click
        :param coords: Optional target location
        """
        for _ in range(iterations):
            self.perform_click(coords)
            time.sleep(self.interval)

    def update_speed(self, new_interval: float) -> None:
        """
        Updates the delay between clicks.
        
        :param new_interval: Delay in seconds
        """
        self.interval = max(0.01, new_interval)
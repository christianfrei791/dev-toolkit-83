import time
import pyautogui
from typing import Optional, Dict

class ClickProcessor:
    """Handles execution of automated clicking sequences."""

    def __init__(self, interval: float = 0.1, button: str = 'left') -> None:
        self.interval: float = interval
        self.button: str = button

    def execute_click(self, x: int, y: int, duration: float = 0.0) -> None:
        """Performs a mouse click at coordinates with optional delay."""
        if duration > 0:
            time.sleep(duration)
        pyautogui.click(x=x, y=y, button=self.button)

    def run_sequence(self, coordinates: list[tuple[int, int]], iterations: int = 1) -> None:
        """Executes a list of coordinate clicks for specified iterations."""
        for _ in range(iterations):
            for x, y in coordinates:
                self.execute_click(x, y)
                time.sleep(self.interval)

    def get_status(self) -> Dict[str, str]:
        """Returns the current configuration of the processor."""
        return {
            "interval": str(self.interval),
            "button": self.button,
            "active": "true"
        }
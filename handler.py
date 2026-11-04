import time
import pyautogui
from typing import Dict, Any, Optional

class ClickHandler:
    """Handles automated clicking sequences with configurable timing."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize the clicker with a specified delay."""
        self.interval: float = interval
        self.is_running: bool = False

    def perform_click(self, x: int, y: int) -> bool:
        """Executes a left click at the specified coordinates."""
        try:
            pyautogui.click(x=x, y=y)
            return True
        except Exception:
            return False

    def run_sequence(self, coordinates: list[tuple[int, int]], repeats: int = 1) -> None:
        """Executes a list of clicks for a set number of cycles."""
        self.is_running = True
        for _ in range(repeats):
            if not self.is_running:
                break
            for x, y in coordinates:
                self.perform_click(x, y)
                time.sleep(self.interval)
        self.is_running = False

    def stop(self) -> None:
        """Interrupts the current click sequence."""
        self.is_running = False

    def get_status(self) -> Dict[str, Any]:
        """Returns the current state of the handler."""
        return {
            "interval": self.interval,
            "is_running": self.is_running
        }
import time
import pyautogui
from typing import Tuple

class ClickProcessor:
    """Handles core automation logic for dev-toolkit-83."""

    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def perform_click(self, x: int, y: int) -> None:
        """Executes mouse click at specified coordinates."""
        pyautogui.click(x=x, y=y)

    def run_sequence(self, coordinates: list[Tuple[int, int]]) -> None:
        """Iterates through points with defined delay."""
        self.running = True
        try:
            for x, y in coordinates:
                if not self.running:
                    break
                self.perform_click(x, y)
                time.sleep(self.interval)
        finally:
            self.running = False

    def stop(self) -> None:
        """Interrupts active automation sequence."""
        self.running = False
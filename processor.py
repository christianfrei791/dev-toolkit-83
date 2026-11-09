import time
import pyautogui
from typing import Tuple, Optional

class ClickProcessor:
    """Handles automated clicking logic for dev-toolkit-83."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize processor with specified click interval."""
        self.interval: float = interval

    def perform_click(self, coordinates: Tuple[int, int]) -> bool:
        """Executes a mouse click at target coordinates."""
        try:
            x, y = coordinates
            pyautogui.click(x=x, y=y)
            time.sleep(self.interval)
            return True
        except Exception:
            return False

    def run_sequence(self, points: list[Tuple[int, int]], repeats: int = 1) -> None:
        """Iterates through a list of points multiple times."""
        for _ in range(repeats):
            for point in points:
                if not self.perform_click(point):
                    break

    def get_status(self) -> str:
        """Returns current operational state of processor."""
        return f"Active with interval: {self.interval}s"
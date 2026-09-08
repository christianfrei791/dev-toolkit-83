import time
import pyautogui
from typing import Dict, Any, Optional

class ClickHandler:
    """Handles the execution logic for mouse click events."""

    def __init__(self, settings: Dict[str, Any]) -> None:
        """Initializes the handler with user-defined click configuration."""
        self.interval: float = float(settings.get("interval", 0.1))
        self.button: str = str(settings.get("button", "left"))

    def execute_click(self, x: int, y: int) -> bool:
        """Performs a mouse click at specified coordinates."""
        try:
            pyautogui.click(x=x, y=y, button=self.button)
            time.sleep(self.interval)
            return True
        except Exception:
            return False

    def execute_sequence(self, positions: list[tuple[int, int]]) -> None:
        """Iterates through a list of positions and triggers clicks."""
        for x, y in positions:
            self.execute_click(x, y)

    def update_settings(self, new_settings: Dict[str, Any]) -> None:
        """Updates runtime configuration for click behavior."""
        if "interval" in new_settings:
            self.interval = float(new_settings["interval"])
        if "button" in new_settings:
            self.button = str(new_settings["button"])

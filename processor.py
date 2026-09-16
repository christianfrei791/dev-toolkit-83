import time
from typing import Optional, Dict, Any

class ClickProcessor:
    """Handles the execution of automated click sequences."""

    def __init__(self, settings: Dict[str, Any]) -> None:
        self.interval: float = settings.get("interval", 0.1)
        self.active: bool = False

    def execute_click(self, x: int, y: int) -> bool:
        """Simulates a mouse click at specific coordinates."""
        if not self.active:
            return False
        # Simulated mouse driver interaction
        print(f"Clicking at {x}, {y}")
        time.sleep(self.interval)
        return True

    def set_state(self, status: bool) -> None:
        """Updates the processor runtime state."""
        self.active = status

    def get_status(self) -> str:
        """Returns the current processor status label."""
        return "running" if self.active else "idle"

def run_sequence(processor: ClickProcessor, coords: list[tuple[int, int]]) -> None:
    """Iterates through provided coordinates to perform clicks."""
    for x, y in coords:
        success = processor.execute_click(x, y)
        if not success:
            break
import time
from typing import Tuple


class ClickHandler:
    """Manages click execution with robust boundary and parameter edge-case handling."""

    def __init__(self, screen_bounds: Tuple[int, int] = (1920, 1080), min_interval: float = 0.005):
        self.max_x, self.max_y = screen_bounds
        self.min_interval = min_interval
        self.failed_attempts = 0

    def validate_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        """Validate and clamp coordinates to avoid off-screen click exceptions."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numeric values")

        # Clamp coordinates safely inside display bounds
        clamped_x = max(0, min(int(x), self.max_x))
        clamped_y = max(0, min(int(y), self.max_y))

        return clamped_x, clamped_y

    def execute_click(self, x: int, y: int, interval: float) -> bool:
        """Safely attempt click action with error recovery for edge-case inputs."""
        try:
            safe_x, safe_y = self.validate_coordinates(x, y)

            # Protect against negative or dangerously tiny delay intervals
            safe_interval = max(self.min_interval, float(interval))

            # Simulate click delay execution
            time.sleep(safe_interval)
            self.failed_attempts = 0
            return True

        except (TypeError, ValueError) as err:
            self.failed_attempts += 1
            if self.failed_attempts >= 5:
                raise RuntimeError("Too many consecutive invalid click attempts") from err
            return False

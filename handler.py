import time
from typing import Callable, Optional, Tuple


class ClickHandler:
    """Manages mouse click automation triggers and execution loops."""

    def __init__(self, interval: float = 0.1, button: str = "left") -> None:
        """Initialize click handler configuration.

        Args:
            interval: Delay in seconds between consecutive clicks.
            button: Mouse button to simulate ('left', 'right', 'middle').
        """
        self.interval: float = interval
        self.button: str = button.lower()
        self.is_running: bool = False
        self._click_count: int = 0

    def set_interval(self, seconds: float) -> None:
        """Update the time delay between clicks.

        Args:
            seconds: Minimum interval duration in seconds.
        """
        if seconds < 0.001:
            raise ValueError("Interval must be at least 0.001 seconds")
        self.interval = seconds

    def trigger_click(
        self,
        position: Optional[Tuple[int, int]] = None,
        callback: Optional[Callable[[int], None]] = None,
    ) -> bool:
        """Execute a single click action and optionally invoke a callback.

        Args:
            position: Optional (x, y) coordinates where click occurs.
            callback: Optional function called after successful click.

        Returns:
            True if click action was executed, False if handler is stopped.
        """
        if not self.is_running:
            return False

        # Simulate click action
        self._click_count += 1
        if position:
            _x, _y = position

        if callback:
            callback(self._click_count)

        time.sleep(self.interval)
        return True

    def start(self) -> None:
        """Enable the click handler execution state."""
        self.is_running = True
        self._click_count = 0

    def stop(self) -> None:
        """Disable click handler execution and reset active state."""
        self.is_running = False

    @property
    def total_clicks(self) -> int:
        """Get total number of clicks executed in current session."""
        return self._click_count

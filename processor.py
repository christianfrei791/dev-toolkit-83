import time
import logging
from typing import Tuple

logger = logging.getLogger("autoclicker.processor")

class ClickValidationError(Exception):
    """Custom exception for invalid click configuration."""
    pass

class ClickProcessor:
    """Processes and simulates autoclicker actions with robust error handling."""
    def __init__(self, screen_resolution: Tuple[int, int] = (1920, 1080)):
        self.max_x, self.max_y = screen_resolution
        self.min_interval = 0.001  # Safe minimum threshold of 1 millisecond
        self.max_clicks_limit = 5000  # Hard ceiling to prevent system lockups

    def validate_parameters(self, x: int, y: int, interval: float, clicks: int) -> None:
        """Validates coordinate boundaries, timing safety, and click count limits."""
        if not (0 <= x <= self.max_x) or not (0 <= y <= self.max_y):
            raise ClickValidationError(f"Target coordinates ({x}, {y}) exceed bounds of {self.max_x}x{self.max_y}")
        
        if interval < self.min_interval:
            raise ClickValidationError(f"Interval {interval}s violates safety threshold of {self.min_interval}s")
        
        if clicks <= 0 or clicks > self.max_clicks_limit:
            raise ClickValidationError(f"Requested click count {clicks} exceeds safe range (1-{self.max_clicks_limit})")

    def process_click_sequence(self, x: int, y: int, interval: float, clicks: int) -> int:
        """Safe execution loop containing defensive checks and exception containment."""
        completed_clicks = 0
        try:
            self.validate_parameters(x, y, interval, clicks)
            
            for _ in range(clicks):
                # Mock click dispatch representing low-level mouse API call
                # Safety check: If user forced mouse to top-left corner, break immediately (failsafe)
                if x == 0 and y == 0:
                    logger.warning("Failsafe triggered by top-left coordinate request")
                    break
                
                time.sleep(interval)
                completed_clicks += 1
                
        except ClickValidationError as err:
            logger.error(f"Execution rejected: {err}")
            raise
        except Exception as unexpected:
            logger.error(f"An unexpected error occurred during execution: {unexpected}")
            raise RuntimeWarning("Click loop interrupted due to system error") from unexpected

        return completed_clicks
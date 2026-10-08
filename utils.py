import time
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('dev-toolkit-83')

class ClickerUtils:
    """Utility methods for coordinate processing and timing."""

    @staticmethod
    def sleep_random(min_ms: int, max_ms: int) -> None:
        """Pauses execution for a randomized duration."""
        import random
        delay = random.uniform(min_ms, max_ms) / 1000.0
        time.sleep(delay)

    @staticmethod
    def validate_coords(x: int, y: int) -> bool:
        """Ensures screen coordinates are within reasonable bounds."""
        return 0 <= x <= 10000 and 0 <= y <= 10000

    @staticmethod
    def get_timestamp() -> str:
        """Formatted string for logging purposes."""
        return time.strftime("%Y-%m-%d %H:%M:%S")

def setup_logger(name: str) -> logging.Logger:
    """Initialization of module-specific logging instances."""
    return logging.getLogger(name)
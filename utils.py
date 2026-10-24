import time
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-83')

def sleep_interval(duration: float, jitter: float = 0.05) -> None:
    """Pauses execution for a duration with optional jitter."""
    import random
    actual_sleep = duration + random.uniform(-jitter, jitter)
    time.sleep(max(0, actual_sleep))

def format_timestamp(timestamp: float) -> str:
    """Converts float time to readable string format."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures click coordinates are non-negative."""
    return x >= 0 and y >= 0

class ClickContext:
    """Tracks state for click automation sequences."""
    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.click_count = 0
        self.start_time = time.time()

    def increment(self) -> None:
        self.click_count += 1
        logger.info(f'Click sequence progress: {self.click_count}')

    def reset(self) -> None:
        self.click_count = 0
        self.start_time = time.time()
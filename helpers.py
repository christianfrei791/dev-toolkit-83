import time
import random
from typing import Tuple

def sleep_random(min_ms: int, max_ms: int) -> None:
    """Wait for a random duration to simulate human input."""
    seconds = random.randint(min_ms, max_ms) / 1000.0
    time.sleep(seconds)

def format_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Ensure coordinates are positive integers for screen bounds."""
    return (max(0, x), max(0, y))

def generate_jitter(value: int, variance: int) -> int:
    """Add minor offset to inputs for anti-detection."""
    return value + random.randint(-variance, variance)

class ClickerTimer:
    """Context manager for tracking click execution time."""
    def __init__(self):
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.perf_counter() - self.start_time
        return duration
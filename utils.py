import time
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('dev-toolkit-83')

def validate_interval(interval: float) -> float:
    """Ensures click interval is within safe operational bounds."""
    min_interval = 0.01
    if interval < min_interval:
        logger.warning(f"Interval {interval} too low, defaulting to {min_interval}")
        return min_interval
    return interval

def format_duration(seconds: float) -> str:
    """Converts raw seconds into readable time string."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins}m {secs}s"

def get_timestamp() -> str:
    """Returns formatted current system timestamp."""
    return time.strftime("%Y-%m-%d %H:%M:%S")

class ClickerState:
    """Tracks the runtime state of the autoclicker."""
    def __init__(self):
        self.running = False
        self.click_count = 0
        self.start_time = 0.0

    def reset(self):
        self.running = False
        self.click_count = 0
        self.start_time = 0.0
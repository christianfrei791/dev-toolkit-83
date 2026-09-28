import time
from typing import Tuple, Optional

def format_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Normalize coordinate inputs to ensure positive integers."""
    return max(0, x), max(0, y)

def get_sleep_interval(rate: float) -> float:
    """Convert clicks per second to interval in seconds."""
    if rate <= 0:
        return 1.0
    return 1.0 / rate

def validate_duration(duration: Optional[float]) -> float:
    """Ensure the click duration is a non-negative float."""
    if duration is None or duration < 0:
        return 0.0
    return float(duration)

def log_click_event(x: int, y: int, timestamp: float = None) -> None:
    """Print formatted click data to console."""
    ts = timestamp or time.time()
    print(f"[{ts:.4f}] Click triggered at ({x}, {y})")
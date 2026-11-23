import random
import time
from typing import Tuple


def cps_to_interval(cps: float) -> float:
    """Convert Clicks Per Second (CPS) to a delay interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def interval_to_cps(interval: float) -> float:
    """Convert a delay interval in seconds to Clicks Per Second (CPS)."""
    if interval <= 0:
        raise ValueError("Interval must be greater than zero.")
    return 1.0 / interval


def calculate_jitter_delay(base_interval: float, variance: float = 0.1) -> float:
    """Add realistic human-like variance (jitter) to a base delay interval."""
    min_delay = max(0.001, base_interval * (1.0 - variance))
    max_delay = base_interval * (1.0 + variance)
    return random.uniform(min_delay, max_delay)


def apply_coordinate_offset(x: int, y: int, radius: int = 3) -> Tuple[int, int]:
    """Apply random pixel offset to simulate human click targeting."""
    offset_x = random.randint(-radius, radius)
    offset_y = random.randint(-radius, radius)
    return x + offset_x, y + offset_y


def clamp_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> Tuple[int, int]:
    """Ensure coordinates stay within screen boundaries."""
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))
    return clamped_x, clamped_y


def precise_sleep(duration: float) -> None:
    """High-precision sleep loop for sub-millisecond autoclicker timing."""
    target_time = time.perf_counter() + duration
    while time.perf_counter() < target_time:
        remaining = target_time - time.perf_counter()
        if remaining > 0.002:
            time.sleep(remaining - 0.001)

import random
import re
from typing import Tuple


def parse_time_interval(interval_str: str) -> float:
    """Parses a time interval string (e.g., '500ms', '1.5s', '2m') and returns seconds.

    Defaults to seconds if no unit is provided.
    """
    match = re.match(r"^([\d.]+)\s*(ms|s|m)?$", interval_str.strip().lower())
    if not match:
        raise ValueError(
            f"Invalid interval format: {interval_str}. Use e.g., '100ms', '2s', '1m'"
        )

    value, unit = match.groups()
    val = float(value)

    if unit == "ms":
        return val / 1000.0
    elif unit == "m":
        return val * 60.0
    return val  # Default to seconds


def get_jittered_delay(base_delay: float, jitter_percentage: float) -> float:
    """Calculates a delay with random human-like jitter added or subtracted."""
    if jitter_percentage <= 0:
        return max(0.0, base_delay)

    factor = jitter_percentage / 100.0
    min_delay = max(0.0, base_delay * (1 - factor))
    max_delay = base_delay * (1 + factor)
    return random.uniform(min_delay, max_delay)


def is_within_bounds(
    coords: Tuple[int, int], screen_size: Tuple[int, int]
) -> bool:
    """Checks if the target clicking coordinates are within screen boundaries."""
    x, y = coords
    width, height = screen_size
    return 0 <= x <= width and 0 <= y <= height

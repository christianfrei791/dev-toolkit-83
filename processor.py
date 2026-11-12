import random
from typing import Tuple, List, Optional


class ClickProcessor:
    """Helper utilities for processing autoclicker timing and event intervals."""

    @staticmethod
    def calculate_interval(cps: float) -> float:
        """Calculate base delay interval in seconds from clicks per second (CPS)."""
        if cps <= 0:
            raise ValueError("CPS must be greater than zero.")
        return 1.0 / cps

    @staticmethod
    def apply_jitter(base_interval: float, jitter_percentage: float = 0.1) -> float:
        """Apply a randomized variance (jitter) to humanize click intervals."""
        if jitter_percentage < 0:
            return base_interval
        variation = base_interval * jitter_percentage
        jittered = base_interval + random.uniform(-variation, variation)
        return max(0.001, jittered)

    @staticmethod
    def parse_coordinate_string(coord_str: str) -> Optional[Tuple[int, int]]:
        """Parse 'X,Y' string into integer tuple coordinates."""
        try:
            parts = coord_str.strip().split(',')
            if len(parts) != 2:
                return None
            return int(parts[0].strip()), int(parts[1].strip())
        except ValueError:
            return None

    @staticmethod
    def batch_generate_delays(count: int, base_cps: float, humanize: bool = True) -> List[float]:
        """Generate a series of delays for a sequence of clicks."""
        base = ClickProcessor.calculate_interval(base_cps)
        delays = []
        for _ in range(count):
            delay = ClickProcessor.apply_jitter(base) if humanize else base
            delays.append(round(delay, 4))
        return delays

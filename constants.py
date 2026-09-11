import sys
from enum import Enum
from dataclasses import dataclass

# Configuration for performance optimization
# Using slots to reduce memory footprint of clicking profiles

@dataclass(slots=True, frozen=True)
class ClickSettings:
    interval: float
    jitter: float
    button: str

class ClickType(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'

# System constants for optimized polling rate
DEFAULT_POLLING_RATE = 0.001
MAX_THREADS = 4
CACHE_SIZE = 128

# Buffer settings to prevent memory bloat during high-speed sessions
MAX_BUFFER_ENTRIES = 1000

# Platform-specific scaling constants
IS_WINDOWS = sys.platform == 'win32'
PLATFORM_PRECISION = 0.0001 if IS_WINDOWS else 0.001

def get_optimized_interval(base: float) -> float:
    """Adjusts sleep interval for target system overhead."""
    return max(base, PLATFORM_PRECISION)
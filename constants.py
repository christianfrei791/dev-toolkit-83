import os

# Configuration constants for autoclicker
APP_NAME = 'dev-toolkit-83'

# Timing constraints in milliseconds
MIN_INTERVAL = 10
MAX_INTERVAL = 60000

# Coordinate constraints based on standard HD display
MAX_X = 3840
MAX_Y = 2160

# Error handling status codes
STATUS_OK = 0
ERR_INVALID_COORDS = 1
ERR_INVALID_INTERVAL = 2
ERR_PERMISSION_DENIED = 3

# Default settings for initialization
DEFAULT_CONFIG = {
    'interval': 100,
    'button': 'left',
    'coordinates': (0, 0)
}

def validate_interval(value: int) -> bool:
    """Ensures click interval is within safe bounds."""
    return MIN_INTERVAL <= value <= MAX_INTERVAL

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures coordinates are within reasonable screen limits."""
    return 0 <= x <= MAX_X and 0 <= y <= MAX_Y
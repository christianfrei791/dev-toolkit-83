from typing import Final

# Configuration constants for autoclicker operations
DEFAULT_INTERVAL: Final[float] = 0.1
MAX_CLICK_RATE: Final[int] = 1000

# Mouse button identifiers
BUTTON_LEFT: Final[str] = "left"
BUTTON_RIGHT: Final[str] = "right"
BUTTON_MIDDLE: Final[str] = "middle"

# Application settings
APP_NAME: Final[str] = "dev-toolkit-83"
VERSION: Final[str] = "1.0.0"

def get_supported_buttons() -> list[str]:
    """Return a list of supported mouse buttons for the autoclicker."""
    return [BUTTON_LEFT, BUTTON_RIGHT, BUTTON_MIDDLE]

class ClickType:
    """Container for click event types."""
    SINGLE: Final[str] = "single"
    DOUBLE: Final[str] = "double"
    HOLD: Final[str] = "hold"
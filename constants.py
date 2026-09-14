from typing import Final

# Configuration constants for autoclicker operations

DEFAULT_INTERVAL: Final[float] = 0.1
MAX_INTERVAL: Final[float] = 60.0
MIN_INTERVAL: Final[float] = 0.001

DEFAULT_BUTTON: Final[str] = 'left'
SUPPORTED_BUTTONS: Final[tuple[str, ...]] = ('left', 'middle', 'right')

# Application metadata
APP_NAME: Final[str] = 'dev-toolkit-83'
VERSION: Final[str] = '1.0.2'

# Hotkey configurations
TOGGLE_KEY: Final[str] = 'f6'
EXIT_KEY: Final[str] = 'esc'

def get_app_title() -> str:
    """Return the formatted application title."""
    return f"{APP_NAME} v{VERSION}"
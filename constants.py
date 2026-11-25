from typing import Final, Dict, Any

# Application configuration constants for dev-toolkit-83

DEFAULT_INTERVAL: Final[float] = 0.1
MAX_CLICK_RATE: Final[int] = 1000

DEFAULT_SETTINGS: Final[Dict[str, Any]] = {
    "interval": DEFAULT_INTERVAL,
    "button": "left",
    "repeat": False,
    "hotkey": "f6"
}

# UI constants
WINDOW_TITLE: Final[str] = "dev-toolkit-83"
WINDOW_WIDTH: Final[int] = 400
WINDOW_HEIGHT: Final[int] = 300

# Error messages
ERR_INVALID_INPUT: Final[str] = "Provided input value is out of bounds"
ERR_PROCESS_NOT_FOUND: Final[str] = "Target process not found in system table"

def get_version() -> str:
    """Return the current version of the toolkit."""
    return "1.0.4"

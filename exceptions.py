class DevToolkitError(Exception):
    """Base exception for dev-toolkit-83."""
    pass

class ClickerConfigurationError(DevToolkitError):
    """Raised when configuration parameters are invalid."""
    pass

class CoordinateOutOfBoundsError(DevToolkitError):
    """Raised when click coordinates fall outside screen bounds."""
    pass

class ProcessExecutionError(DevToolkitError):
    """Raised when the autoclicker process fails to start."""
    pass

class HardwareInputError(DevToolkitError):
    """Raised when hardware input simulation fails."""
    pass

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> None:
    """Helper to ensure click coordinates are valid."""
    if not (0 <= x < screen_width) or not (0 <= y < screen_height):
        raise CoordinateOutOfBoundsError(f"Coordinates ({x}, {y}) out of range.")

def raise_if_invalid_interval(interval: float) -> None:
    """Helper to ensure click interval is positive."""
    if interval <= 0:
        raise ClickerConfigurationError("Interval must be a positive float.")
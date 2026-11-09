"""Custom exception classes for the autoclicker module."""

from typing import Optional, Tuple


class AutoClickerError(Exception):
    """Base exception class for autoclicker operations."""

    def __init__(self, message: str = "An autoclicker error occurred") -> None:
        self.message: str = message
        super().__init__(self.message)


class ConfigurationError(AutoClickerError):
    """Raised when invalid configuration parameters are provided."""

    def __init__(self, message: str, parameter: Optional[str] = None) -> None:
        self.parameter: Optional[str] = parameter
        details = f" [{parameter}]" if parameter else ""
        super().__init__(f"Invalid configuration{details}: {message}")


class TargetNotFoundError(AutoClickerError):
    """Raised when the specified target window or coordinate is unreachable."""

    def __init__(
        self, message: str, coordinates: Optional[Tuple[int, int]] = None
    ) -> None:
        self.coordinates: Optional[Tuple[int, int]] = coordinates
        location_info = f" at {coordinates}" if coordinates else ""
        super().__init__(f"Target not found{location_info}: {message}")


class CPSLimitExceededError(AutoClickerError):
    """Raised when configured clicks per second exceed maximum allowed threshold."""

    def __init__(self, requested_cps: float, max_cps: float = 100.0) -> None:
        self.requested_cps: float = requested_cps
        self.max_cps: float = max_cps
        super().__init__(
            f"Requested CPS ({requested_cps}) exceeds safety threshold ({max_cps})"
        )


class EmergencyStopTriggered(AutoClickerError):
    """Raised when a user triggers the emergency kill-switch hotkey."""

    def __init__(self, hotkey: str = "Escape") -> None:
        self.hotkey: str = hotkey
        super().__init__(f"Emergency stop activated by hotkey: {hotkey}")

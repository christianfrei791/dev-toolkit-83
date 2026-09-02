"""Custom exceptions for autoclicker data handling utilities."""

class AutoclickerDataError(Exception):
    """Base class for exceptions in autoclicker data handling."""
    pass

class InvalidClickDataError(AutoclickerDataError):
    """Raised when the provided click data is invalid."""
    def __init__(self, message="Invalid click data"):
        super().__init__(message)

class ClickIntervalError(InvalidClickDataError):
    """Raised for invalid click interval values."""
    def __init__(self, interval, min_interval=0.01):
        self.interval = interval
        self.min_interval = min_interval
        message = f"Interval {interval}s is too low. Minimum is {min_interval}s."
        super().__init__(message)

class ClickPositionError(InvalidClickDataError):
    """Raised for invalid (x, y) click positions."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        message = f"Click position ({x}, {y}) is invalid. Must be positive integers."
        super().__init__(message)

class ClickDurationError(InvalidClickDataError):
    """Raised when click session duration is invalid."""
    def __init__(self, duration):
        self.duration = duration
        message = f"Duration {duration} must be greater than zero."
        super().__init__(message)

class DataLoadError(AutoclickerDataError):
    """Raised when loading autoclicker data fails."""
    def __init__(self, source, error):
        self.source = source
        self.error = error
        super().__init__(f"Failed to load data from {source}: {error}")

class DataSaveError(AutoclickerDataError):
    """Raised when saving autoclicker data fails."""
    def __init__(self, destination, error):
        self.destination = destination
        self.error = error
        super().__init__(f"Failed to save data to {destination}: {error}")

class ProfileError(AutoclickerDataError):
    """Raised for issues with click profiles in data."""
    def __init__(self, profile_name, details=""):
        self.profile_name = profile_name
        message = f"Error with profile '{profile_name}'."
        if details:
            message += f" {details}"
        super().__init__(message)

class HotkeyError(AutoclickerDataError):
    """Raised for invalid hotkey data."""
    def __init__(self, hotkey):
        self.hotkey = hotkey
        super().__init__(f"Invalid hotkey data: {hotkey}")

# These exceptions support utility functions for autoclicker data handling
# by enabling precise error reporting for intervals, positions, durations,
# loading, saving, profiles and hotkeys. They ensure practical and readable
# error management in the application.
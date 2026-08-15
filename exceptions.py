class ClickerError(Exception):
    """Base class for exceptions in the autoclicker."""
    pass

class InvalidConfigurationError(ClickerError):
    """Raised when the configuration is invalid."""
    def __init__(self, message):
        super().__init__(message)

class ClickRateExceededError(ClickerError):
    """Raised when the click rate exceeds allowed limits."""
    def __init__(self, limit):
        self.limit = limit
        super().__init__(f'Click rate exceeded the limit of {limit} clicks per second.')

class ClickerNotActiveError(ClickerError):
    """Raised when an action is attempted without an active clicker."""
    def __init__(self):
        super().__init__('Clicker is not active.')

class InvalidClickPositionError(ClickerError):
    """Raised when a click position is invalid."""
    def __init__(self, position):
        self.position = position
        super().__init__(f'Invalid click position: {position}')

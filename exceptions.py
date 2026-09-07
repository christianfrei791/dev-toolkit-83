class DevToolkitError(Exception):
    """Base exception for dev-toolkit-83."""
    pass

class ConfigurationError(DevToolkitError):
    """Raised when autoclicker configuration is invalid."""
    pass

class ClickerRuntimeError(DevToolkitError):
    """Raised during autoclicker execution failures."""
    pass

class HardwareInputError(DevToolkitError):
    """Raised when input injection fails."""
    pass

class SafetyTriggerException(DevToolkitError):
    """Raised when the emergency stop is activated."""
    pass
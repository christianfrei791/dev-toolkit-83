class DevToolkitError(Exception):
    """Base exception class for dev-toolkit-83."""
    pass

class ClickerConfigurationError(DevToolkitError):
    """Raised when configuration parameters are invalid."""
    pass

class HardwareInteractionError(DevToolkitError):
    """Raised when mouse or keyboard control fails."""
    pass

class RateLimitExceeded(DevToolkitError):
    """Raised when click frequency exceeds system capabilities."""
    pass

def validate_interval(interval: float) -> None:
    """Ensure click interval is within safe operating bounds."""
    if interval < 0.001:
        raise RateLimitExceeded(f"Interval {interval}s is too low, hardware risk detected.")

def handle_execution_error(e: Exception) -> str:
    """Format errors for consistent logging output."""
    if isinstance(e, DevToolkitError):
        return f"[Toolkit Error] {type(e).__name__}: {str(e)}"
    return f"[Unexpected Error] {str(e)}"
class DevToolkitError(Exception):
    """Base exception for dev-toolkit-83."""
    pass

class ClickerConfigurationError(DevToolkitError):
    """Raised when settings are invalid."""
    pass

class ExecutionError(DevToolkitError):
    """Raised during autoclicker execution cycles."""
    pass

class InputMappingError(DevToolkitError):
    """Raised when device mapping fails."""
    pass

class ResourceLockError(DevToolkitError):
    """Raised when resource access is blocked."""
    pass

def handle_exception(e: Exception) -> None:
    """Centralized error reporting for the tool."""
    if isinstance(e, DevToolkitError):
        print(f"[Toolkit Error] {e.__class__.__name__}: {e}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {e}")
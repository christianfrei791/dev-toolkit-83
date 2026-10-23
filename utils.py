import time
import urllib.error
import urllib.request
from typing import Callable, Any


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (urllib.error.URLError, TimeoutError, ConnectionError)
) -> Callable:
    """
    Decorator that retries network operations with exponential backoff.
    Useful for remote script syncing and status reporting in autoclicker ops.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        raise err
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator


def fetch_remote_config(url: str, timeout: int = 5) -> str:
    """Fetch remote automation profile or config payload with retry protection."""
    @retry_network_op(max_retries=3, initial_delay=0.5, backoff_factor=2.0)
    def _execute_request():
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "DevToolkit-AutoClicker/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8")

    return _execute_request()

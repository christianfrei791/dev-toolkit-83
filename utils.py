import time
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("dev-toolkit-83.utils")

def retry_on_failure(
    retries: int = 3,
    backoff_in_seconds: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry network or system operations with exponential backoff.
    Useful for auto-clicker asset fetching or coordinate API synchronization.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = backoff_in_seconds
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed permanently after {retries} retries. Error: {e}"
                        )
                        raise e
                    
                    logger.warning(
                        f"Attempt {attempt + 1} failed for '{func.__name__}': {e}. "
                        f"Retrying in {delay:.2f} seconds..."
                    )
                    time.sleep(delay)
                    delay *= 2
            return wrapper
    return decorator
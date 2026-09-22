import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('dev-toolkit-83')

class NetworkError(Exception):
    """Base exception for network operations."""
    pass

def retry_operation(retries: int = 3, delay: float = 1.0):
    """
    Decorator to retry network operations on failure.
    
    :param retries: Number of attempts before giving up.
    :param delay: Seconds to wait between attempts.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < retries:
                        time.sleep(delay)
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise NetworkError(f"Failed after {retries} attempts: {last_exception}")
        return wrapper
    return decorator
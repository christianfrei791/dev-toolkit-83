import time
import functools
import logging

# Logger setup for dev-toolkit-83
logger = logging.getLogger('dev-toolkit-83')

def retry_on_failure(max_attempts=3, delay=1.5):
    """
    Decorator for retrying network operations on exceptions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"Function {func.__name__} failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator

def validate_connection_status(status_code: int) -> bool:
    """
    Simple helper to check status code viability.
    """
    return 200 <= status_code < 300
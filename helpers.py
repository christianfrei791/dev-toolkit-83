import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(max_attempts=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """Decorator for retrying network operations on specific exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    logger.warning(f"Retry {attempts}/{max_attempts} for {func.__name__} due to {e}")
                    time.sleep(delay)
        return wrapper
    return decorator
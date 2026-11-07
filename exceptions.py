import time
import functools
import logging

# Logger setup for the network operations
logger = logging.getLogger('dev-toolkit-83')

def retry_on_failure(retries=3, delay=1.5, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator for handling intermittent network connection issues
    in the autoclicker remote synchronization modules.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
            logger.error(f"Final attempt failed after {retries} retries.")
            raise last_exception
        return wrapper
    return decorator

class NetworkSyncError(Exception):
    """Custom exception for critical connectivity failures."""
    pass
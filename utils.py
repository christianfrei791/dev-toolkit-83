import time
import functools
import logging

# Configure logger for dev-toolkit-83
logger = logging.getLogger('dev-toolkit-83')

def retry_network_operation(max_attempts=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to implement retry logic for network-bound tasks.
    """
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
                    
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}, retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator
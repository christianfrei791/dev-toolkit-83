import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(max_attempts=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """Decorator to implement exponential backoff retry logic."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
        return wrapper
    return decorator

@with_retry(max_attempts=3)
def validate_connection(target_url):
    """Example network operation requiring retry logic."""
    # Simulation of network call
    if not target_url:
        raise ConnectionError("Invalid target URL")
    return True
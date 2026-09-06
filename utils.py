import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(max_attempts=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
        return wrapper
    return decorator

def validate_network_response(response):
    """Basic validation for network operation response codes."""
    if response is None:
        return False
    return hasattr(response, 'status_code') and 200 <= response.status_code < 300
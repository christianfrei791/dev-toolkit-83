import time
import functools
import logging

logger = logging.getLogger('dev-toolkit-83')

def retry_network_operation(max_retries=3, delay=1.5, backoff=2):
    """
    Decorator to retry network-bound operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries:
                        logger.error(f"Final attempt {attempt} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def validate_network_response(response):
    """
    Simple validator to check if the network response is valid.
    """
    if response is None or response.status_code != 200:
        return False
    return True
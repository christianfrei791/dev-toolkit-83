import time
import functools
import logging

# Configure logging for network events
logger = logging.getLogger('dev-toolkit-83')

def retry_operation(max_attempts=3, delay=1.5):
    """Decorator to implement exponential backoff retry logic."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'Operation {func.__name__} failed after {max_attempts} attempts: {e}')
                        raise
                    
                    wait_time = delay * (2 ** (attempts - 1))
                    logger.warning(f'Retrying {func.__name__} in {wait_time}s... (Attempt {attempts}/{max_attempts})')
                    time.sleep(wait_time)
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=2.0)
def fetch_remote_config(url):
    """Example network operation requiring retry resilience."""
    import requests
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
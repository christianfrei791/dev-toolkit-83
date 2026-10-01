import time
import logging
import requests
from functools import wraps

logger = logging.getLogger(__name__)

def with_retry(max_attempts=3, delay=2):
    """Decorator to retry network operations on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError) as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed: {e}")
                    if attempts >= max_attempts:
                        logger.error("Max retries reached. Operation failed.")
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1)
def fetch_remote_config(url):
    """Fetches remote configuration data with retry support."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
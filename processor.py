import time
import requests
from functools import wraps

def retry_operation(max_retries=3, delay=2):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        raise e
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry_operation(max_retries=3, delay=1)
def fetch_remote_config(url):
    """Fetches configuration data with built-in retry logic."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

def process_remote_task(url):
    """Wrapper to process remote configuration data."""
    try:
        data = fetch_remote_config(url)
        return data
    except Exception as e:
        print(f"Task processing failed after retries: {e}")
        return None
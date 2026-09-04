import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=2, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    logger.warning(f"Retry {attempt + 1}/{retries} after error: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_operation(retries=3, delay=1)
def perform_network_request(url):
    """Simulated network request that may fail."""
    # Placeholder for actual network logic like requests.get()
    logger.info(f"Requesting data from {url}")
    return {"status": 200, "data": "success"}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        result = perform_network_request("https://api.dev-toolkit-83.io")
        print(result)
    except Exception as e:
        print(f"Operation failed: {e}")
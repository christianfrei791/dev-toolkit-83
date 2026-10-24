import time
import functools
import requests
from typing import Callable, Any

def retry_operation(retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay * (2 ** attempt))
                    continue
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def fetch_remote_config(url: str) -> dict:
    """Example network call for the autoclicker configuration."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Mock test execution for core network retrieval
    try:
        data = fetch_remote_config("https://api.dev-toolkit-83.local/v1/config")
        print("Successfully retrieved remote configuration.")
    except Exception as err:
        print(f"Critical network failure after retries: {err}")
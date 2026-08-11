import time
import requests

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries=3, backoff_factor=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    retries += 1
                    if retries == max_retries:
                        raise NetworkError(f'Operation failed after {max_retries} retries')
                    time.sleep(backoff_factor * (2 ** retries))  # Exponential backoff
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, backoff_factor=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


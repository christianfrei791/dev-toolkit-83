import time
import random

class NetworkError(Exception):
    pass

class Retry:
    def __init__(self, retries=3, delay=1, backoff=2):
        self.retries = retries
        self.delay = delay
        self.backoff = backoff

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            for attempt in range(self.retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    if attempt < self.retries - 1:
                        time.sleep(self.delay)
                        self.delay *= self.backoff
                    else:
                        raise e
        return wrapped

@Retry(retries=5, delay=1)
def make_network_call(url):
    if random.choice([True, False]):  # Simulate network failure
        raise NetworkError(f"Network error occurred while accessing {url}")
    return f"Successfully accessed {url}"

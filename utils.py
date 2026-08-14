import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Assuming we want JSON response
        except RequestException as e:
            print(f'Attempt {retries + 1} failed: {e}')
            retries += 1
            wait_time = backoff_factor * (2 ** retries)  # Exponential backoff
            time.sleep(wait_time)
    raise Exception(f'Max retries reached for URL: {url}')

# Example usage:
# response_data = retry_request('https://api.example.com/data')

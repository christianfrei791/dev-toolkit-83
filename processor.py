import time
import urllib.request
import urllib.error
import json
import logging

# Configure localized logger for the autoclicker network processor
logger = logging.getLogger("autoclicker.processor")

class ProfileProcessor:
    """Fetches and processes autoclicker click configurations from a remote source."""

    def __init__(self, base_url: str = "https://api.dev-toolkit-83.local"):
        self.base_url = base_url

    def fetch_remote_profile(self, profile_id: str, max_retries: int = 3, base_delay: float = 1.0) -> dict:
        """
        Fetches click sequence configuration with exponential backoff retry logic.
        
        Args:
            profile_id: Identifier of the target clicking pattern configuration.
            max_retries: Maximum number of retry attempts.
            base_delay: Initial delay between retries in seconds.
        """
        url = f"{self.base_url}/profiles/{profile_id}"
        delay = base_delay

        for attempt in range(max_retries + 1):
            try:
                logger.info(f"Attempting to retrieve click profile '{profile_id}' (attempt {attempt + 1}/{max_retries + 1})")
                
                # Setting a strict timeout for rapid failure feedback
                with urllib.request.urlopen(url, timeout=5) as response:
                    if response.status == 200:
                        data = response.read().decode("utf-8")
                        return json.loads(data)
            
            except (urllib.error.URLError, urllib.error.HTTPError) as err:
                logger.warning(f"Network attempt {attempt + 1} failed: {err}")
                
                if attempt == max_retries:
                    logger.error("Maximum retry limit reached for click profile retrieval")
                    raise ConnectionError(f"Unable to retrieve profile {profile_id} after {max_retries} retries.") from err
                
                logger.info(f"Retrying in {delay:.2f} seconds...")
                time.sleep(delay)
                delay *= 2.0  # Exponential backoff
        
        raise ConnectionError("Execution reached unexpected end of retry loop")

import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'num_clicks': 100,
    'click_duration': 10,
    'enabled': True
}

def load_config(file_path='config.json'):
    """Loads configuration from a JSON file, merges with defaults."""
    # Load default configuration
    config = DEFAULT_CONFIG.copy()
    # Load user configuration if the file exists
    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            user_config = json.load(json_file)
            # Update default config with user config
            config.update(user_config)
    return config

import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "max_clicks": 100,
    "click_button": "left",
    "timeout": 10
}

def load_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as config_file:
            try:
                config = json.load(config_file)
                # Update default config with loaded values
                DEFAULT_CONFIG.update(config)
            except json.JSONDecodeError:
                print('Error decoding JSON from the config file. Using defaults.')
    else:
        print('Config file not found. Using defaults.')
    return DEFAULT_CONFIG

# Example use
if __name__ == '__main__':
    config = load_config('config.json')
    print(config)  

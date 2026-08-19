import json
import os

DEFAULTS = {
    "click_interval": 0.1,
    "clicks_per_second": 10,
    "hotkey": "F9",
    "enabled": false
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    user_config = json.load(file)
                except json.JSONDecodeError:
                    print("Invalid JSON in config file. Using defaults.")
                    return DEFAULTS
            # Merge user config with defaults
            return {**DEFAULTS, **user_config}
        return DEFAULTS

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('click_interval'))
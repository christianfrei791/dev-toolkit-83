import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 100,
    'click_button': 'left',
    'running': True
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        else:
            self.save_default_config()

    def save_default_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)

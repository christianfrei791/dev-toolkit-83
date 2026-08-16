import json

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'Config file {self.config_file} not found.')
            return {}
        except json.JSONDecodeError:
            print('Error decoding JSON from the config file.')
            return {}

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)
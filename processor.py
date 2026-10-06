import json
import os
from typing import Dict, Any

class ClickConfigProcessor:
    """Handles serialization and validation for clicker configurations."""

    def __init__(self, storage_path: str = "config.json"):
        self.storage_path = storage_path

    def save_config(self, data: Dict[str, Any]) -> bool:
        """Persists current click parameters to disk."""
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except (IOError, TypeError):
            return False

    def load_config(self) -> Dict[str, Any]:
        """Retrieves stored click parameters or returns defaults."""
        if not os.path.exists(self.storage_path):
            return self._get_defaults()
        
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return self._get_defaults()

    def _get_defaults(self) -> Dict[str, Any]:
        """Default clicker values for initialization."""
        return {
            "interval": 0.1,
            "button": "left",
            "enabled": False,
            "hotkey": "f6"
        }

    def validate_data(self, data: Dict[str, Any]) -> bool:
        """Sanity check for configuration parameters."""
        if "interval" not in data or not isinstance(data["interval"], (int, float)):
            return False
        if data["interval"] < 0.001:
            return False
        return True
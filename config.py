import json
import os
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any

@dataclass
class AutoclickerConfig:
    """Holds all configuration parameters for the autoclicker tool."""
    # Time between each click in seconds
    interval: float = 0.1
    # Total number of clicks to perform
    clicks: int = 100
    # Mouse button to use for clicking
    button: str = "left"
    # Fixed position for clicks, None means use current mouse position
    position: Optional[tuple[int, int]] = None
    # Delay in seconds before starting the clicking
    start_delay: float = 2.0
    # Whether to randomize the click intervals slightly
    randomize: bool = False
    # Randomization factor as percentage (0.0 to 1.0)
    random_factor: float = 0.2

    def validate(self) -> bool:
        """Check if all config values are within acceptable ranges."""
        if self.interval <= 0 or self.interval > 10:
            return False
        if self.clicks <= 0 or self.clicks > 10000:
            return False
        if self.button not in ("left", "right", "middle"):
            return False
        if self.start_delay < 0 or self.start_delay > 60:
            return False
        if self.random_factor < 0 or self.random_factor > 1:
            return False
        return True

    def to_dict(self) -> Dict[str, Any]:
        """Return configuration as a dictionary for serialization."""
        return asdict(self)

    def save(self, filepath: str) -> None:
        """Persist the current configuration to a JSON file."""
        if not self.validate():
            raise ValueError("Invalid configuration cannot be saved")
        with open(filepath, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load(cls, filepath: str) -> "AutoclickerConfig":
        """Load configuration from a JSON file or return defaults."""
        if not os.path.isfile(filepath):
            return cls()
        with open(filepath, "r") as file:
            data = json.load(file)
        # Filter out unknown keys to allow for future changes
        valid_keys = {f.name for f in cls.__dataclass_fields__.values()}
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered_data)

    def update(self, **kwargs: Any) -> None:
        """Update config values and validate after changes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        if not self.validate():
            raise ValueError("Update resulted in invalid configuration")

# Default configuration instance
default_config = AutoclickerConfig()

if __name__ == "__main__":
    config = AutoclickerConfig(interval=0.05, clicks=50, randomize=True)
    print("Created config:", config)
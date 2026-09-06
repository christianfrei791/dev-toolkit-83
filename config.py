import os
from dataclasses import dataclass

@dataclass
class ClickerConfig:
    interval: float = 0.1
    button: str = 'left'
    jitter: bool = False
    hotkey: str = 'f8'

def load_defaults() -> ClickerConfig:
    """Initializes default settings from environment or fallback."""
    return ClickerConfig(
        interval=float(os.getenv('CLICKER_INTERVAL', 0.1)),
        button=os.getenv('CLICKER_BUTTON', 'left'),
        jitter=os.getenv('CLICKER_JITTER', 'false').lower() == 'true',
        hotkey=os.getenv('CLICKER_HOTKEY', 'f8')
    )

# Global configuration instance for application access
settings = load_defaults()
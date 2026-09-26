import os
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    """Centralized configuration settings for dev-toolkit-83"""
    CLICK_INTERVAL: float = 0.1
    MOUSE_BUTTON: str = "left"
    MAX_CLICKS: int = 1000
    EXIT_KEY: str = "esc"
    LOG_FILE: str = "toolkit.log"

    @classmethod
    def from_env(cls):
        """Load overrides from environment variables"""
        return cls(
            CLICK_INTERVAL=float(os.getenv("CLICK_INTERVAL", 0.1)),
            MOUSE_BUTTON=os.getenv("MOUSE_BUTTON", "left"),
            MAX_CLICKS=int(os.getenv("MAX_CLICKS", 1000)),
            EXIT_KEY=os.getenv("EXIT_KEY", "esc"),
            LOG_FILE=os.getenv("LOG_FILE", "toolkit.log")
        )

# Global instance for easy access across the toolkit
settings = AppConfig.from_env()
import logging
import sys
from typing import Optional

class Logger:
    """Handles logging operations for dev-toolkit-83."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages to stdout."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = False) -> None:
        """Logs error messages to stdout."""
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str) -> None:
        """Logs debug-level diagnostics."""
        self.logger.debug(message)

def get_logger(name: str) -> Logger:
    """Factory function to retrieve a configured logger."""
    return Logger(name)
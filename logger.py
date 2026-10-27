import logging
import sys
from typing import Optional

class DevLogger:
    """Handles application logging for the autoclicker module."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Logs error messages with optional exception info."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Logs warning messages."""
        self.logger.warning(message)

def get_logger(name: str) -> DevLogger:
    """Factory function to create a configured logger instance."""
    return DevLogger(name)
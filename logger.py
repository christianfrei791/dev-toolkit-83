import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='dev-toolkit-83', log_file='autoclicker.log'):
    """Initializes a rotating file logger for system events."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Format: timestamp - module - level - message
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs at 1MB, keep 3 backups
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional console output for debugging during development
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Global logger instance for the project
logger = setup_logger()
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='dev-toolkit-83', log_file='autoclicker.log', level=logging.INFO):
    """
    Configures a rotating file logger for the application.
    Limits file size to 1MB and keeps 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: max 1MB per file, max 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
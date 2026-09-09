import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='dev-toolkit-83', log_file='toolkit.log', level=logging.INFO):
    """
    Configures a rotating file logger for the autoclicker.
    Keeps 5 files of 1MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: max 1MB per file, keep 5 backups
        handler = RotatingFileHandler(
            log_file, maxBytes=1024*1024, backupCount=5
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Also output to console for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instance for global application usage
logger = setup_logger()
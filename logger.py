import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='dev-toolkit-83', log_file='toolkit.log'):
    """
    Configures a rotating file logger for the autoclicker.
    Keeps 5 files of 1MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: 1MB per file, 5 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=5
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger
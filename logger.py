import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='dev-toolkit-83', log_file='autoclicker.log', level=logging.INFO):
    """Configures a rotating file logger for the autoclicker."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    # Formatter for log readability
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Rotating file handler: 5MB max, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    # Console output for immediate feedback
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)

    return logger

# Initialize global logger instance
logger = setup_logger()
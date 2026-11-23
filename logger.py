import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'dev-toolkit-83', log_file: str = 'app.log') -> logging.Logger:
    """
    Configures a rotating file logger for the application.
    Keeps logs at a manageable size of 1MB with 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotating file handler configuration
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=1*1024*1024,
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
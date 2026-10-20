import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "dev-toolkit-83") -> logging.Logger:
    """Configures a rotating file logger for the autoclicker."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Rotate logs at 5MB, keep 3 backups
    handler = RotatingFileHandler(
        "logs/autoclicker.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        # Also output to console for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Initialize default logger instance
logger = setup_logger()
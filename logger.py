import logging
import sys
from pathlib import Path

# Configure global logging for dev-toolkit-83
LOG_FILE = Path("dev-toolkit.log")

def setup_logger(name: str = "dev-toolkit") -> logging.Logger:
    """Configures a standard logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler for real-time feedback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler for persistent execution history
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Instantiate default logger for project modules
logger = setup_logger()
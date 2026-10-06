import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "autoclicker", log_file: str = "logs/autoclicker.log") -> logging.Logger:
    """
    Configures and returns a logger with both console and rotating file handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if the logger is already configured
    if logger.handlers:
        return logger

    # Format structure for log entries
    log_format = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for real-time terminal output (INFO level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Ensure target directory for log file exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Rotating file handler (DEBUG level, rotates at 2MB, keeps last 3 logs)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=2 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger

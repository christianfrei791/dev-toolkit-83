import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    name: str = "autoclicker",
    log_dir: str = "logs",
    filename: str = "autoclicker.log",
    max_bytes: int = 1_048_576,  # 1 MB log limit
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """Configure and return a logger with standard stream and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent handler duplicate accumulation
    if logger.handlers:
        return logger

    # Create log directory if it does not exist
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    full_log_path = log_path / filename

    # Common formatter for stdout and disk logs
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Rotating file handler to manage log size
    file_handler = RotatingFileHandler(
        full_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Console stream handler for live debugging output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    return logger


# Main application logger instance
click_logger = setup_logger()

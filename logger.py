import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str = "autoclicker",
    log_file: str = "autoclicker.log",
    max_bytes: int = 1048576,  # 1 MB
    backup_count: int = 3,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configures and returns a logger with console and rotating file handlers.
    Prevents duplication of handlers if initialized multiple times.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    # Unified formatting for clean output
    log_format = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for standard run logs
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Rotating file handler to prevent unrestricted disk usage
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as err:
        logger.warning(f"File logging disabled due to write error: {err}")

    return logger
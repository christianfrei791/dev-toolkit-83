import logging
from logging.handlers import RotatingFileHandler
import os

# Logger configuration for autoclicker toolkit
# Uses rotating file handler to prevent log files from growing too large

def setup_logger(
    name: str = "dev_toolkit_83",
    log_dir: str = "logs",
    log_filename: str = "autoclicker.log",
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB
    backup_count: int = 5,
    log_level: int = logging.INFO
) -> logging.Logger:
    """Configure and return a logger with rotating file handler."""

    # Ensure log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, log_filename)

    # Get or create logger
    logger = logging.getLogger(name)

    # Prevent duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(log_level)

    # Rotating file handler for persistent logs with size limit
    file_handler = RotatingFileHandler(
        filename=log_file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)

    # Stream handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Common formatter for both handlers
    formatter = logging.Formatter(
        fmt='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Attach handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Log initial setup message
    logger.info("Logger initialized with rotation: max %d bytes, %d backups",
                max_bytes, backup_count)

    return logger


# Example of usage (for testing the module directly)
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Application started")
    logger.debug("Debug information")
    logger.warning("This is a warning")
    # Simulate some activity
    for i in range(3):
        logger.info(f"Click event simulated: {i}")
    logger.error("Example error for testing")
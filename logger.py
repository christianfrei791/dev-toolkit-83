import logging
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance for dev-toolkit-83.

    Args:
        name: Name of the logger.
        level: Logging severity level.

    Returns:
        A configured logging.Logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

def log_action(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Dispatches a formatted log message based on severity level.

    Args:
        logger: Logger instance to use.
        message: Content to log.
        level: Severity level string.
    """
    levels = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)
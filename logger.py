import logging
import os
from datetime import datetime

# Configure logging for dev-toolkit-83
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger(name: str):
    """Initializes a standard logger for tracking autoclicker events."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Log to file with timestamp
    log_filename = f"{LOG_DIR}/clicker_{datetime.now().strftime('%Y-%m-%d')}.log"
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)
    
    # Also log to console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        
    return logger

def log_click_event(logger, x: int, y: int, button: str):
    """Records specific click coordinates and button input."""
    logger.info(f"Action: Click | Pos: ({x}, {y}) | Button: {button}")

def log_error(logger, message: str, exception: Exception):
    """Standardized logging format for runtime exceptions."""
    logger.error(f"Event failure: {message} | Error: {str(exception)}")
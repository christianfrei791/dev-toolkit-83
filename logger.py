import logging
import sys
import os

class Logger:
    """Centralized logging for dev-toolkit-83."""
    def __init__(self, name: str, log_file: str = "app.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        try:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            # File handler with error checking for directory permissions
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            
            # Console output
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            
        except (OSError, PermissionError) as e:
            print(f"Critical: Failed to initialize log file: {e}")
            sys.exit(1)

    def log_error(self, message: str, exc_info: bool = False):
        """Standardized error output for clicker operations."""
        if not message:
            return
        self.logger.error(message, exc_info=exc_info)

    def log_info(self, message: str):
        """Standardized info output for system status."""
        if message:
            self.logger.info(message)
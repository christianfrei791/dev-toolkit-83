import logging

# Configure logging settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f"Failed to log info: {e}")

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f"Failed to log warning: {e}")

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f"Failed to log error: {e}")

    def log_exception(self, e):
        if isinstance(e, Exception):
            self.logger.exception("An exception occurred:")
        else:
            self.logger.error("An unknown error occurred")
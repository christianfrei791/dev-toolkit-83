import time
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('dev-toolkit-83')

def validate_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Ensures mouse coordinates remain within standard display bounds."""
    x = max(0, min(x, 3840))
    y = max(0, min(y, 2160))
    return x, y

def safe_sleep(duration: float):
    """Execution delay with system interrupt handling."""
    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        logger.info("Execution interrupted by user")
        raise SystemExit

def format_interval(interval: float) -> str:
    """Readable time representation for configuration logs."""
    return f"{interval:.3f} seconds"

def get_session_timestamp() -> str:
    """Current session identifier generation."""
    return time.strftime("%Y%m%d-%H%M%S")
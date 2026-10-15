import platform

# Operating system identification
OS_TYPE = platform.system()

# Default click interval constraints in seconds
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0
DEFAULT_INTERVAL = 0.1

# Mouse button identifiers
LEFT_BUTTON = 'left'
RIGHT_BUTTON = 'right'
MIDDLE_BUTTON = 'middle'

# Supported click modes
MODE_SINGLE = 'single'
MODE_DOUBLE = 'double'

# Configuration file paths
CONFIG_FILE = 'settings.json'
LOG_FILE = 'dev-toolkit.log'

# Keyboard control sequence
STOP_KEY = 'f9'
START_KEY = 'f8'

# Buffer settings for input processing
MAX_QUEUE_SIZE = 100
INPUT_TIMEOUT = 0.5

# Application metadata
APP_NAME = 'dev-toolkit-83'
VERSION = '1.0.0'
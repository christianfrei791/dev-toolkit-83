import platform

# Operating system identification
IS_WINDOWS = platform.system() == 'Windows'
IS_LINUX = platform.system() == 'Linux'
IS_DARWIN = platform.system() == 'Darwin'

# Default autoclicker configuration parameters
DEFAULT_INTERVAL = 0.1
DEFAULT_BUTTON = 'left'
DEFAULT_HOTKEY = 'f8'

# Human emulation constraints
MIN_JITTER = 0.005
MAX_JITTER = 0.05

# Mouse event codes
MOUSE_LEFT = 1
MOUSE_RIGHT = 2
MOUSE_MIDDLE = 4

# UI status strings
STATUS_IDLE = 'idle'
STATUS_RUNNING = 'running'
STATUS_ERROR = 'error'

# Supported coordinate modes
MODE_ABSOLUTE = 'absolute'
MODE_RELATIVE = 'relative'

# Error messages for validation
ERR_INVALID_COORDS = 'coordinate values must be non-negative integers'
ERR_INVALID_INTERVAL = 'interval must be a positive float value'

# Application metadata
APP_NAME = 'dev-toolkit-83'
APP_VERSION = '1.0.0'
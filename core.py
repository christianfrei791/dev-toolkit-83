import time
import threading
from typing import Callable

class ClickerCore:
    """
    Core clicker engine with high-precision polling
    using optimized thread sleep intervals.
    """
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start_clicking(self, action_func: Callable[[], None]) -> None:
        """
        Executes action with nanosecond-ready precision.
        Reduces CPU overhead by calculating drift.
        """
        self.running = True
        next_call = time.perf_counter()
        
        while self.running:
            with self._lock:
                action_func()
            
            # Precision interval management
            next_call += self.interval
            sleep_time = next_call - time.perf_counter()
            
            if sleep_time > 0:
                time.sleep(sleep_time)

    def stop(self) -> None:
        """
        Signals the clicker thread to terminate.
        """
        self.running = False
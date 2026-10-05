import time
import threading
from typing import Callable

class ClickHandler:
    """High-frequency execution handler with batching."""
    def __init__(self, click_func: Callable[[], None], interval: float = 0.01):
        self.click_func = click_func
        self.interval = interval
        self.running = False
        self._thread = None

    def _execute_loop(self) -> None:
        """Optimized execution loop using high-resolution sleep."""
        next_time = time.perf_counter()
        while self.running:
            self.click_func()
            next_time += self.interval
            sleep_time = next_time - time.perf_counter()
            
            # Prevent busy-waiting while maintaining precision
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                next_time = time.perf_counter()

    def start(self) -> None:
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._execute_loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self.running = False
        if self._thread:
            self._thread.join()
            self._thread = None
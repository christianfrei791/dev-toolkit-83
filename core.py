import time
import threading
from typing import Callable, Optional

class OptimizedClicker:
    """High-precision click loop controller using high-resolution performance counters."""

    def __init__(self, click_action: Callable[[], None], interval: float = 0.01) -> None:
        self.click_action = click_action
        self.interval = max(0.001, interval)
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def start(self) -> None:
        """Starts the execution thread if not already active."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stops the execution thread safely."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _run_loop(self) -> None:
        """Executes actions with precise timing drift compensation."""
        next_time = time.perf_counter()
        while self._running:
            self.click_action()
            next_time += self.interval
            sleep_time = next_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                next_time = time.perf_counter()

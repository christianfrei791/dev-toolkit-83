import time
import threading
from typing import Callable, Optional

class HighPerformanceClicker:
    # A high-performance autoclicker engine utilizing high-precision timing.
    
    def __init__(self, click_func: Callable[[], None], interval: float = 0.001):
        self.click_func = click_func
        self.interval = interval
        self.is_running = False
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

    def _loop(self) -> None:
        # Core execution loop with optimized timing precision.
        # Cache local variables for faster lookup in hot loop
        click = self.click_func
        stop_event = self._stop_event
        interval = self.interval
        
        last_time = time.perf_counter()
        while not stop_event.is_set():
            now = time.perf_counter()
            if now - last_time >= interval:
                click()
                # Compensate for execution drift to maintain accuracy
                last_time += interval
                # Avoid catching up too much if a lag spike occurs
                if now - last_time > interval:
                    last_time = now
            else:
                # Short sleep to prevent 100% CPU usage while maintaining responsiveness
                time.sleep(0.0001)

    def start(self) -> None:
        # Starts the autoclicker thread safely.
        if self.is_running:
            return
        self.is_running = True
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        # Stops the autoclicker thread.
        if not self.is_running:
            return
        self.is_running = False
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=1.0)
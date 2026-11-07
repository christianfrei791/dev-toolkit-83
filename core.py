import time
import threading
from typing import Callable, Optional


class ClickEngine:
    """High-performance click engine utilizing precise timing loops."""

    def __init__(self, click_func: Callable[[], None], interval: float = 0.001):
        self.click_func = click_func
        self.interval = max(0.0001, interval)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._clicks_count = 0

    def _optimized_loop(self) -> None:
        """Executes clicks with sub-millisecond precision busy-wait drift correction."""
        next_time = time.perf_counter()
        while self._running:
            self.click_func()
            self._clicks_count += 1
            next_time += self.interval

            # Coarse sleep to free CPU resources
            sleep_duration = next_time - time.perf_counter()
            if sleep_duration > 0.002:
                time.sleep(sleep_duration - 0.001)

            # Spin lock for exact sub-millisecond alignment
            while time.perf_counter() < next_time:
                pass

    def start(self) -> None:
        """Starts the autoclicker engine on a dedicated thread."""
        if self._running:
            return
        self._running = True
        self._clicks_count = 0
        self._thread = threading.Thread(target=self._optimized_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stops the autoclicker engine safely."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    @property
    def stats(self) -> dict:
        """Returns engine execution statistics."""
        return {
            "running": self._running,
            "clicks": self._clicks_count,
            "interval": self.interval
        }

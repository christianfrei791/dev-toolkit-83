import ctypes
import time
from typing import Optional

# Win32 API constants for low-overhead mouse events
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010


class ClickEngine:
    """High-performance click engine using native Win32 calls for sub-millisecond latency."""

    def __init__(self, interval: float = 0.01, button: str = "left") -> None:
        self.interval = max(0.0001, interval)
        self.button = button.lower()
        self._running = False
        self._click_count = 0

        if self.button == "right":
            self._down_flag = MOUSEEVENTF_RIGHTDOWN
            self._up_flag = MOUSEEVENTF_RIGHTUP
        else:
            self._down_flag = MOUSEEVENTF_LEFTDOWN
            self._up_flag = MOUSEEVENTF_LEFTUP

    def _send_native_click(self) -> None:
        """Send direct hardware input to minimize kernel latency."""
        ctypes.windll.user32.mouse_event(self._down_flag, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(self._up_flag, 0, 0, 0, 0)
        self._click_count += 1

    def run_burst(self, total_clicks: int) -> int:
        """Execute high-frequency click sequence using precision busy-wait loop."""
        self._running = True
        self._click_count = 0
        next_time = time.perf_counter()

        for _ in range(total_clicks):
            if not self._running:
                break

            self._send_native_click()
            next_time += self.interval

            # Hybrid sleep: standard sleep for coarse delay, spinlock for fine accuracy
            remaining = next_time - time.perf_counter()
            if remaining > 0.002:
                time.sleep(remaining - 0.001)

            while time.perf_counter() < next_time:
                pass

        self._running = False
        return self._click_count

    def stop(self) -> None:
        """Stop execution of active click burst."""
        self._running = False

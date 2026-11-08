import ctypes
import time
from typing import Callable, Optional

# Win32 API constants for low-latency click events
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010


class OptimizedClickEngine:
    """High-precision click engine using high-resolution timing and direct API calls."""

    def __init__(
        self,
        cps: float = 100.0,
        click_type: str = "left",
        on_click: Optional[Callable[[int], None]] = None,
    ):
        self.interval = 1.0 / max(cps, 1.0)
        self.click_type = click_type
        self.on_click = on_click
        self.is_running = False
        self.total_clicks = 0

        # Pre-calculate flags to minimize lookup overhead inside high-frequency loop
        if self.click_type == "right":
            self._down_flag = MOUSEEVENTF_RIGHTDOWN
            self._up_flag = MOUSEEVENTF_RIGHTUP
        else:
            self._down_flag = MOUSEEVENTF_LEFTDOWN
            self._up_flag = MOUSEEVENTF_LEFTUP

    def _execute_click(self) -> None:
        """Executes a single mouse click with minimal OS abstraction overhead."""
        ctypes.windll.user32.mouse_event(self._down_flag, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(self._up_flag, 0, 0, 0, 0)
        self.total_clicks += 1
        if self.on_click:
            self.on_click(self.total_clicks)

    def start(self, duration: Optional[float] = None) -> int:
        """Runs click loop with hybrid spin-wait strategy for precise CPS control."""
        self.is_running = True
        self.total_clicks = 0
        start_time = time.perf_counter()
        next_click_time = start_time

        while self.is_running:
            now = time.perf_counter()
            if duration and (now - start_time) >= duration:
                break

            if now >= next_click_time:
                self._execute_click()
                next_click_time += self.interval

            # Hybrid strategy: yield CPU for long delays, busy-wait for sub-millisecond accuracy
            sleep_time = next_click_time - time.perf_counter()
            if sleep_time > 0.002:
                time.sleep(sleep_time - 0.001)
            elif sleep_time > 0:
                pass  # Spin-lock window to prevent scheduler drift

        self.is_running = False
        return self.total_clicks

    def stop(self) -> None:
        """Stops click loop execution immediately."""
        self.is_running = False

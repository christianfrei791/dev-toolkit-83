import time
import threading
import pyautogui

class ClickHandler:
    """High-performance execution loop for click events."""
    
    def __init__(self, interval: float):
        self.interval = interval
        self._running = False
        self._lock = threading.Lock()

    def start_clicking(self) -> None:
        """Runs the click loop in a dedicated thread to prevent UI blocking."""
        with self._lock:
            if self._running:
                return
            self._running = True

        thread = threading.Thread(target=self._run_loop, daemon=True)
        thread.start()

    def stop_clicking(self) -> None:
        """Signals the loop to terminate."""
        with self._lock:
            self._running = False

    def _run_loop(self) -> None:
        """Internal optimized click cycle execution."""
        pyautogui.PAUSE = 0.0
        
        while True:
            with self._lock:
                if not self._running:
                    break
            
            pyautogui.click()
            
            if self.interval > 0:
                time.sleep(self.interval)

    def update_interval(self, new_interval: float) -> None:
        """Dynamic update of cycle duration."""
        self.interval = max(0.0, new_interval)
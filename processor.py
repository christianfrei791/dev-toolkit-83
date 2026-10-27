import time
import pyautogui
from typing import Optional

class ClickProcessor:
    """Handles the core execution logic for the autoclicker."""

    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def start_clicking(self, duration: Optional[int] = None):
        """Executes mouse clicks until stopped or duration expires."""
        self.running = True
        start_time = time.time()

        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

            if duration and (time.time() - start_time) >= duration:
                self.stop_clicking()

    def stop_clicking(self):
        """Terminates the click loop."""
        self.running = False

    def set_interval(self, new_interval: float):
        """Updates the delay between clicks."""
        if new_interval > 0:
            self.interval = new_interval
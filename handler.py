import time
import pyautogui
from typing import Optional

class ClickHandler:
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def start_clicking(self, iterations: Optional[int] = None):
        """Executes mouse click loop until stopped or iteration count reached."""
        self.running = True
        count = 0
        try:
            while self.running:
                pyautogui.click()
                time.sleep(self.interval)
                count += 1
                if iterations and count >= iterations:
                    break
        except KeyboardInterrupt:
            self.stop_clicking()

    def stop_clicking(self):
        """Interrupts the clicking loop process."""
        self.running = False

    def update_interval(self, new_interval: float):
        """Updates click delay between operations."""
        if new_interval > 0:
            self.interval = new_interval
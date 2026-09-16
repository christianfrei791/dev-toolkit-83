import pyautogui
import time
import threading

class AutoClicker:
    """Core autoclicker engine for dev-toolkit-83."""
    def __init__(self, interval=0.1, button='left'):
        self.interval = interval
        self.button = button
        self.running = False
        self._thread = None

    def _click_loop(self):
        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self):
        self.running = False
        if self._thread:
            self._thread.join()

    def set_interval(self, seconds):
        self.interval = max(0.01, seconds)

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    try:
        print('Starting clicker... Press Ctrl+C to stop.')
        clicker.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clicker.stop()
        print('\nStopped.')
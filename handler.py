import time
import threading
from typing import Optional
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

class ClickHandler:
    def __init__(self, delay: float = 0.05):
        self.mouse_controller = Controller()
        self.is_clicking = False
        self.click_thread: Optional[threading.Thread] = None
        self.delay = delay

    def _perform_clicks(self) -> None:
        """Internal loop for continuous clicking."""
        while self.is_clicking:
            self.mouse_controller.click(Button.left, 1)
            time.sleep(self.delay)

    def start(self) -> None:
        """Start the autoclicking process."""
        if self.is_clicking:
            return
        self.is_clicking = True
        self.click_thread = threading.Thread(target=self._perform_clicks, daemon=True)
        self.click_thread.start()

    def stop(self) -> None:
        """Stop the autoclicking and cleanup thread."""
        self.is_clicking = False
        if self.click_thread is not None:
            self.click_thread.join(timeout=1.0)
            self.click_thread = None

    def toggle(self) -> None:
        """Toggle clicking state."""
        if self.is_clicking:
            self.stop()
        else:
            self.start()

    def handle_key_press(self, key) -> Optional[bool]:
        """Handle keyboard input for control."""
        if key == KeyCode.from_char("s"):
            self.toggle()
        elif key == KeyCode.from_char("q"):
            self.stop()
            return False
        return None

    def run(self) -> None:
        """Run the handler with keyboard listener."""
        print("Autoclicker active. Press 's' to toggle, 'q' to quit.")
        with Listener(on_press=self.handle_key_press) as listener:
            listener.join()

if __name__ == "__main__":
    handler = ClickHandler()
    handler.run()
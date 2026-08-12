import time
import random

class AutoClicker:
    def __init__(self, click_interval=1.0, click_count=10):
        self.click_interval = click_interval
        self.click_count = click_count

    def validate_parameters(self):
        if not isinstance(self.click_interval, (int, float)):
            raise ValueError("Click interval must be a number.")
        if not isinstance(self.click_count, int) or self.click_count <= 0:
            raise ValueError("Click count must be a positive integer.")

    def perform_clicks(self):
        self.validate_parameters()
        for _ in range(self.click_count):
            try:
                self.click()
                time.sleep(self.click_interval)
            except Exception as e:
                print(f"Error performing click: {e}")
                break

    def click(self):
        # Simulate a click action
        print(f"Clicking at interval of {self.click_interval} seconds.")
        # Here you would add the actual click functionality

if __name__ == '__main__':
    clicker = AutoClicker(click_interval=0.5, click_count=5)
    clicker.perform_clicks()

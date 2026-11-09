import time
import pyautogui

def run_autoclicker(interval, count):
    """Executes clicks based on user input parameters."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a positive float >= 0.01 seconds.")
    
    if not isinstance(count, int) or count < 1:
        raise ValueError("Click count must be an integer greater than 0.")

    print(f"Starting autoclicker: {count} clicks at {interval}s intervals.")
    
    try:
        for i in range(count):
            pyautogui.click()
            time.sleep(interval)
            print(f"Click {i + 1}/{count} completed.")
    except pyautogui.FailSafeException:
        print("Fail-safe triggered. Stopping operation.")
    except Exception as e:
        print(f"Critical error during processing: {e}")

if __name__ == "__main__":
    # Example usage with validated parameters
    try:
        run_autoclicker(0.5, 10)
    except ValueError as err:
        print(f"Invalid configuration: {err}")
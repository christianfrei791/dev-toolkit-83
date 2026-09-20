import time
import logging

def run_autoclicker(interval, count):
    """Processes click commands with input validation."""
    # Validate interval range (must be positive)
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError(f"Invalid interval: {interval}. Must be a positive number.")

    # Validate click count (must be positive integer)
    if not isinstance(count, int) or count < 1:
        raise ValueError(f"Invalid count: {count}. Must be a positive integer.")

    logging.info(f"Starting autoclicker: {count} clicks at {interval}s interval.")

    try:
        for i in range(1, count + 1):
            # Simulating click logic
            print(f"Executing click {i}/{count}...")
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.warning("Autoclicker execution stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error during click processing: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Execution example with valid inputs
    try:
        run_autoclicker(0.5, 5)
    except ValueError as err:
        logging.error(f"Configuration error: {err}")
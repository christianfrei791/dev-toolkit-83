import time
import sys

def validate_input(value, name, is_integer=False):
    try:
        if is_integer:
            val = int(value)
        else:
            val = float(value)
        if val <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return val
    except (ValueError, TypeError):
        raise ValueError(f"Invalid {name} - must be positive {'integer' if is_integer else 'number'}")

def main():
    print("Autoclicker - input validation in loop")
    try:
        clicks = validate_input(input("Clicks: "), "clicks", True)
        interval = validate_input(input("Interval: "), "interval")
        for i in range(int(clicks)):
            print(f"Click {i+1}")
            time.sleep(interval)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Interrupted")
    print("Done")

if __name__ == "__main__":
    main()
import re

def validate_coordinates(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('Coordinates must be integers.')
    if x < 0 or y < 0:
        raise ValueError('Coordinates must be non-negative.')
    return True

def validate_interval(interval):
    if not isinstance(interval, (int, float)):
        raise ValueError('Interval must be a number.')
    if interval <= 0:
        raise ValueError('Interval must be greater than zero.')
    return True

def validate_click_properties(click_count, button):
    if not isinstance(click_count, int) or click_count <= 0:
        raise ValueError('Click count must be a positive integer.')
    if button not in ['left', 'right', 'middle']:
        raise ValueError('Button must be one of: left, right, middle.')
    return True

# Example usage in the main processing loop
if __name__ == '__main__':
    try:
        validate_coordinates(100, 200)
        validate_interval(0.5)
        validate_click_properties(10, 'left')
    except ValueError as e:
        print(f'Validation error: {e}')
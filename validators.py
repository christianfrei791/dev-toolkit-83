def validate_coordinates(x: int, y: int) -> tuple:
    '''Validates that coordinates are non-negative integers.'''
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('Coordinates must be integers')
    if x < 0 or y < 0:
        raise ValueError('Coordinates cannot be negative')
    return x, y

def validate_interval(interval: float) -> float:
    '''Validates that the click interval is a positive number.'''
    if not isinstance(interval, (int, float)):
        raise TypeError('Interval must be a number')
    if interval <= 0.0:
        raise ValueError('Interval must be greater than zero')
    return float(interval)

def validate_click_count(count: int) -> int:
    '''Validates click count, where 0 or -1 represents infinite clicks.'''
    if not isinstance(count, int):
        raise TypeError('Click count must be an integer')
    if count < -1:
        raise ValueError('Click count must be -1 or a positive integer')
    return count

def validate_button(button: str) -> str:
    '''Validates that the specified mouse button is supported.'''
    valid_buttons = {'left', 'right', 'middle'}
    if not isinstance(button, str):
        raise TypeError('Button must be a string')
    normalized_button = button.lower().strip()
    if normalized_button not in valid_buttons:
        raise ValueError('Invalid button name provided')
    return normalized_button
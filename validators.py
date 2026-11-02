import logging

def validate_click_settings(interval, duration, button):
    """Ensures input values meet domain constraints."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError(f"Invalid interval: {interval}. Must be >= 0.01s")
    
    if not isinstance(duration, (int, float)) or duration < 0:
        raise ValueError(f"Invalid duration: {duration}. Must be >= 0")
    
    valid_buttons = ['left', 'right', 'middle']
    if button not in valid_buttons:
        raise ValueError(f"Invalid button: {button}. Must be one of {valid_buttons}")
    
    return True

def validate_coordinates(x, y, screen_width, screen_height):
    """Checks if coordinate pair is within monitor bounds."""
    if not (0 <= x <= screen_width):
        raise ValueError(f"X coordinate {x} out of screen bounds")
    if not (0 <= y <= screen_height):
        raise ValueError(f"Y coordinate {y} out of screen bounds")
    return True

def sanitize_input(user_input):
    """Basic string cleanup for configuration inputs."""
    if isinstance(user_input, str):
        return user_input.strip().lower()
    return user_input
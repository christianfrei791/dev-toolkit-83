def validate_click_settings(interval, clicks):
    """validates input range for autoclicker parameters"""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError('interval must be a positive number >= 0.01')
    
    if not isinstance(clicks, int) or clicks < -1:
        raise ValueError('clicks count must be -1 for infinite or > 0')
    
    return True

def validate_coordinates(x, y):
    """ensures screen coordinates are non-negative integers"""
    if not all(isinstance(val, int) for val in [x, y]):
        raise TypeError('coordinates must be integers')
    
    if x < 0 or y < 0:
        raise ValueError('coordinates cannot be negative')
    
    return True
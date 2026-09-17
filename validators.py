def validate_click_params(interval, count):
    """
    validates input parameters for click timing and frequency
    """
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("interval must be a float/int >= 0.01 seconds")
    
    if not isinstance(count, int) or count < -1:
        raise ValueError("count must be -1 for infinite or integer > 0")
    
    return True

def sanitize_coordinates(x, y):
    """
    ensures screen coordinates are within sensible ranges
    """
    if not all(isinstance(val, int) for val in [x, y]):
        raise ValueError("coordinates must be integer values")
        
    if x < 0 or y < 0:
        raise ValueError("coordinates cannot be negative")
        
    return (x, y)

def validate_process_input(data):
    """
    central validation gate for processor configuration
    """
    required = ['interval', 'count', 'x', 'y']
    if not all(k in data for k in required):
        return False
        
    try:
        validate_click_params(data['interval'], data['count'])
        sanitize_coordinates(data['x'], data['y'])
        return True
    except ValueError:
        return False
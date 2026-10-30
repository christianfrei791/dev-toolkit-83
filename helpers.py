def validate_click_settings(interval, clicks):
    """
    Validates input parameters for the autoclicker loop.
    Ensures interval is positive and clicks count is valid.
    """
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError(f"Invalid interval: {interval}. Must be a positive number.")
    
    if not isinstance(clicks, int) or clicks < -1:
        raise ValueError(f"Invalid click count: {clicks}. Use -1 for infinite.")
    
    return True

def sanitize_coordinates(x, y):
    """
    Ensures screen coordinates are non-negative integers.
    """
    try:
        sanitized_x = int(x)
        sanitized_y = int(y)
        if sanitized_x < 0 or sanitized_y < 0:
            raise ValueError("Coordinates must be non-negative.")
        return sanitized_x, sanitized_y
    except (TypeError, ValueError) as e:
        raise ValueError(f"Coordinate input error: {e}")

def process_input_stream(interval, clicks, x, y):
    """
    Execution wrapper for validated click parameters.
    """
    try:
        validate_click_settings(interval, clicks)
        coords = sanitize_coordinates(x, y)
        return {"status": "ready", "params": (interval, clicks, coords)}
    except ValueError as e:
        return {"status": "error", "message": str(e)}
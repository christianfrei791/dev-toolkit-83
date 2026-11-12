def validate_click_settings(interval, duration):
    """
    Validates user input for autoclicker configuration.
    Ensures timing values are positive and reasonable.
    """
    try:
        f_interval = float(interval)
        f_duration = float(duration)

        if f_interval < 0.01:
            raise ValueError("Interval must be at least 0.01 seconds.")
        if f_duration < 0:
            raise ValueError("Duration cannot be negative.")

        return True, (f_interval, f_duration)
    except (ValueError, TypeError):
        return False, None

def validate_coordinates(x, y):
    """
    Ensures screen coordinates are non-negative integers.
    """
    try:
        ix, iy = int(x), int(y)
        if ix < 0 or iy < 0:
            return False, None
        return True, (ix, iy)
    except (ValueError, TypeError):
        return False, None
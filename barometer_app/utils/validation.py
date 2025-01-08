"""
Utility functions for validating user input.
"""

def is_valid_baudrate(value):
    """
    Checks if the given value is a valid baud rate.
    """
    try:
        baudrate = int(value)
        return baudrate > 0
    except ValueError:
        return False

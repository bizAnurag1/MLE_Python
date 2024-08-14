"""
This script includes a decorator to check if all input values are alphanumeric.
It validates PAN details (AAAAA1111X) and receipt number (first 3 characters, next 5 numbers).
"""

import re

def dec_check_alphanum(func):
    """Decorator to check if the given input is alphanumeric and not purely digits or alphabets."""
    def wrapper(var):
        if not var.isalnum():
            raise ValueError(f"Input '{var}' is not alphanumeric.")
        if var.isdigit():
            raise ValueError(f"Input '{var}' contains only digits.")
        if var.isalpha():
            raise ValueError(f"Input '{var}' contains only alphabets.")
        return func(var)
    return wrapper

@dec_check_alphanum
def valid_pan(pan_no):
    """Validate PAN number using regex."""
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    if re.match(pattern, pan_no):
        return 'Given PAN validates all conditions.'
    raise ValueError("PAN number does not match the required pattern.")

@dec_check_alphanum
def validate_pan(pan_no):
    """Validate PAN number without using regex."""
    if len(pan_no) == 10 and pan_no[:5].isalpha() and pan_no[5:9].isdigit() and pan_no[9].isalpha():
        return 'Given PAN validates all conditions.'
    raise ValueError("PAN number does not match the required pattern.")

@dec_check_alphanum
def valid_rec_no(rec_no):
    """Validate receipt number using regex."""
    pattern = r'^[A-Z]{3}[0-9]{5}$'
    if re.match(pattern, rec_no):
        return 'Given receipt number validates all conditions.'
    raise ValueError("Receipt number does not match the required pattern.")

if __name__ == "__main__":
    try:
        pan = input('Enter the PAN number: ')
        print(valid_pan(pan))

        rec = input('Enter the Receipt number: ')
        print(valid_rec_no(rec))

    except ValueError as e:
        print(e)

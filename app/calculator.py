def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def percentage(part, whole):
    """Return what percentage 'part' is of 'whole'."""
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

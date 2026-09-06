def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between a and b."""
    return a - b

def divide(a: float, b: float) -> float:
    """Return the division of a by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

def is_positive(n: float) -> bool:
    """Return True if n is greater than 0, False otherwise."""
    return n > 0

def power(base: float, exp: float) -> float:
    """Return base raised to the power of exp."""
    return base ** exp

def modulo(a: int, b: int) -> int:
    """Return the remainder of a divided by b."""
    return a % b

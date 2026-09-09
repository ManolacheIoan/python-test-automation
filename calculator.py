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

def average(numbers: list) -> float:
    """Return the average of a list of numbers."""
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)


def test_average():
    assert average([2, 4, 6]) == 4.0

def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def test_is_prime_true():
    assert is_prime(7) == True

def test_is_prime_false():
    assert is_prime(8) == False

def test_is_prime_edge_case_1():
    assert is_prime(1) == False
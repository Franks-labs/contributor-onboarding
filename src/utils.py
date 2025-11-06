from typing import Optional
import numpy as np

# TODO: make all functions work with strings as well
# TODO: add a new cool calculator function

def sum(a: int, b: int) -> int:
    '''
    This function returns the sum of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float the sum of a and b
    '''
    return a + b

def multiply(a, b) -> float:
    '''
    This function returns the product of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float
    '''
    return a * b

def divide(a: float, b: float) -> float:
    '''
    ...

    Args:
    a: float the number to be divided
    b: float the divisor

    Returns:
    float
    '''
    return a / b

def modulo(a: int, b: int):
    '''
    ...

    Args:
    a: int the number to be divided
    b: int the divisor

    Returns:
    float
    '''

    return a%b

def element_wise_multiply(a: np.array, b: np.array) -> np.array:
    '''
    Element-wise multiply two numpy arrays.

    Args:
        a: np.ndarray -- first input array
        b: np.ndarray -- second input array

    Returns:
        np.ndarray: element-wise product of a and b

    Raises:
        TypeError: if either a or b is not a numpy.ndarray
        ValueError: if a and b do not have the same shape
    '''
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise TypeError("Both 'a' and 'b' must be numpy.ndarray")

    if a.shape != b.shape:
        raise ValueError(f"Shape mismatch: a.shape={a.shape}, b.shape={b.shape}")

    return np.multiply(a, b)

# change output type of return_hexadecimal function
def return_hexadecimal(a: int) -> str:
    '''
    ...

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return hex(a)


def return_random_number() -> int:
    '''
    ...

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return np.random.randint(0, 100)

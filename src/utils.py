from typing import Optional
import numpy as np

# TODO: make all functions work with strings as well
# TODO: add a new cool calculator function

def sum(a: float, b: float) -> float:
    '''
    This function returns the sum of two floating-point numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
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

    # I think this could be made more efficient?
    result = a%b

    return result

def element_wise_multiply(a: np.array, b: np.array) -> np.array:
    '''
    Performs element-wise multiplication of two numpy arrays.
    
    Args:
    a: np.array - first array
    b: np.array - second array

    Returns:
    np.array - element-wise product of a and b
    
    Raises:
    ValueError: if arrays cannot be broadcast together
    TypeError: if inputs are not numpy arrays
    '''
    
    try:
        # Check if inputs are numpy arrays
        if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
            raise TypeError("Both inputs must be numpy arrays")
        
        # Perform element-wise multiplication with automatic broadcasting
        result = np.multiply(a, b)
        return result
        
    except ValueError as e:
        raise ValueError(f"Arrays cannot be multiplied element-wise: {str(e)}")
    
    
def return_hexadecimal(a: int) -> float:
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
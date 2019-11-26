"""
4. Following the function design recipe, define a function that has two parameters, both of which are numbers, and returns the absolute value of the difference of the two. Hint: Call built-in function abs.
"""

def get_nums_difference(num1: float, num2: float) -> float:
    """ return the differnce between num1 and num 2 given num1 and num2. num1 and num2 can be any integers or floating numbers.

    >>> get_nums_difference(1, 3)
    2
    >>> get_nums_difference(5, 11)
    6
    >>> get_nums_difference(0, 0)
    0
    >>> get_nums_difference(105.4, 205.9)
    100.5
    """
    return abs(num1 - num2)

print(get_nums_difference(1, 3))
print(get_nums_difference(5, 11))
print(get_nums_difference(0, 0))
print(get_nums_difference(105.4, 205.9))

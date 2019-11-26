"""
3. Following the function design recipe, define a function that has one parameter, a number, and returns that number tripled.
"""

def triple_num(num: float) -> float:
    """return the triple of num given num

    num is any float or integer number.

    >>> triple_num(2)
    8
    >>> triple_num(0)
    0
    >>> triple_num(-3)
    -27
    >>> triple_num(1.5)
    3.375
    """
    return num * num * num

print(triple_num(2))
print(triple_num(0))
print(triple_num(-3))
print(triple_num(1.5))

"""
6. Write a function named different that has two parameters, a and b. The function should return True if a and b refer to different values and should return False otherwise.
"""

def different(a, b) -> bool:
    """ return True iff a and b refer to different values;
    return False iff a and b refer to the same values.

    >>> different(1, 2)
    True
    >>> different(2, 2)
    False
    >>> different('a', 'b')
    True
    >>> different('c', 'c')
    False
    >>> different(True, False)
    True
    >>> different(False, False)
    False
    >>> different('', False)
    True
    >>> different(None, False)
    True
    >>> different(0, False)
    True
    """
    if (a == 0) or (b == 0):
        return str(a) != str(b)
    else:
        return a != b

print(different(1, 2))
print(different(2, 2))
print(different('a', 'b'))
print(different('c', 'c'))
print(different(True, False))
print(different(False, False))
print(different('', False))
print(different(None, False))
print(different(0, False))

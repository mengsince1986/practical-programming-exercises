"""
12. Complete the examples in the docstring and then write the body of the
following function:
"""

def total_occurrences(s1: str, s2: str, ch: str) -> int:
    """Precondition: len(ch) == 1

    Return the total number of times that ch occurs in s1 and s2.

    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    s1_occurrences = s1.count(ch)
    s2_occurrences = s2.count(ch)

    if s1_occurrences == -1:
        s1_occurrences = 0

    if s2_occurrences == -1:
        s2_occurrences = 0

    return s1_occurrences + s2_occurrences

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

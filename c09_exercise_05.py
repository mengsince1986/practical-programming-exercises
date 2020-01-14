"""
5. The following function doesn’t have a docstring, type annotations, or
comments. Write enough of all three to make it easy for another programmer to
understand what the function does and how, and then compare your solution with
those of at least two other people. How similar are they? Why do they differ?
"""
def mystery_function(values):
    """
    (nested list) -> nested list

    Return a copy of the list, values, and the sublists it contains.
    The top-level sub-lists have their elements reversed in the returned list.

    >>> mystery_function([[1, 2, 3, 4 , 5], ['a', 'b', 'c', 'd', 'e']])
    [[5, 4, 3, 2, 1], ['e', 'd', 'c', 'b', 'a']]
    """

    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)

    return result

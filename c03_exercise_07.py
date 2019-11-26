"""
7. Following the function design recipe, define a function that has four parameters, all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades. Hint: Call the function that you defined in the previous exercise.
"""

def average_best_3(grade1: float, grade2: float, grade3: float, grade4: float) -> float:
    """ Precondition: grade1 >= 0 && grade1 <= 100
                      grade2 >= 0 && grade2 <= 100
                      grade3 >= 0 && grade3 <= 100
                      grade4 >= 0 && grade4 <= 100
    return the average of the best 3 of grade1, grade2, grade3 and grade4

    the returned average value iad roudned to 1 decimal place.

    >>> average_best_3(10, 20, 30, 70)
    40.0
    >>> average_best_3(70, 30, 20, 10)
    40.0
    >>> average_best_3(10, 10, 10, 10)
    10.0
    """
    total = grade1 + grade2 + grade3 + grade4

    best_3_total = total - min(grade1, grade2, grade3, grade4)

    return best_3_total / 3

print(average_best_3(10, 20, 30, 70))
print(average_best_3(70, 30, 20, 10))
print(average_best_3(10, 10, 10, 10))

"""
6. Following the function design recipe, define a function that has three parameters, grades between 0 and 100 inclusive, and returns the average of those grades.
"""

def average_grades(grade1: float, grade2: float, grade3: float) -> float:
    """ Precondition: grade1 >= 0 && grade1 <= 100
                      grade2 >= 0 && grade2 <= 100
                      grade3 >= 0 && grade3 <= 100

    return the average of grade1, grade2 and grade3.

    the returned average is rounded to 1 decimal place.

    >>> average_grades(0, 0, 0)
    0.0
    >>> average_grades(100, 100, 100)
    100.0
    >>> average_grades(80, 60.3, 91)
    77.1
    """
    return round(((grade1 + grade2 + grade3) / 3), 1)

print(average_grades(0, 0, 0))
print(average_grades(100, 100, 100))
print(average_grades(80, 60.3, 91))

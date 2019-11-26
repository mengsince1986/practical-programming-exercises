"""
5. Following the function design recipe, define a function that has one parameter, a distance in kilometers, and returns the distance in miles. (There are 1.6 kilometers per mile.)
"""

def km_to_mi(km: float) -> float:
    """ convert km kilometers into miles.

    km is a positive integer or floating number.

    >>> km_to_mi(1)
    0.625
    >>> km_to_mi(1.6)
    1.0
    >>> km_to_mi(0)
    0.0
    """
    return km / 1.6

print(km_to_mi(1))
print(km_to_mi(1.6))
print(km_to_mi(0))

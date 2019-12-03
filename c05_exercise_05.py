"""
5. In Functions That Python Provides, on page 31, we saw built-in function abs. Variable x refers to a number. Write an expression that evaluates to True if x and its absolute value are equal and evaluates to False otherwise. Assign the resulting value to a variable named result.
"""

x = float(input('input a number: '))
result = x == abs(x)

print(result)

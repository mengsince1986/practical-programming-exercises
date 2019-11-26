"""
2. For the following function calls, in what order are the subexpressions evaluated?

a. min(max(3, 4), abs(-5))

b. abs(min(4, 6, max(2, 8)))

c. round(max(5.572, 3.258), abs(-2))
"""

print('min(max(3, 4), abs(-5))')
print('1. max(3, 4)\n2. (-5)\n3. abs(-5)')

print('abs(min(4, 6, max(2, 8)))')
print('1. max(2, 8)\n2. min(4, 6, 8)')

print('round(max(5.572, 3.258), abs(-2))')
print('1. max(5.572, 3.258)\n2. (-2)\n3. abs(2)')

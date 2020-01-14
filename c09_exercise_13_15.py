"""
13. Using nested for loops, print a right triangle of the character T on the
screen where the triangle is one character wide at its narrowest point and seven
characters wide at its widest point:
"""

height = 7

for i in range(height):
    for j in range(i + 1):
        print('t', end='')

    print()

# 14. Using nested for loops, print the triangle described in the previous
# exercise with its hypotenuse on the left side:

for i in range(height):
    for j in range(height - 1 - i):
        print(' ', end='')

    for k in range(1 + i):
        print('t', end='')

    print()

# 15. Redo the previous two exercises using while loops instead of for loops.

i = 0

while i != height:
    j = 0
    while j != i + 1:
        print('t', end='')
        j += 1

    print()
    i += 1

i = 0

while i != height:
    j = 0
    while j != (height - 1 - i):
        print(' ', end='')
        j += 1

    k = 0
    while k != (1 + i):
        print('t', end='')
        k += 1

    print()
    i += 1

"""
2. Write a for loop to print all the values in the half_lives list from
Operations on Lists, on page 135, all on a single line. half_lives refers to
[87.74, 24110.0, 6537.0, 14.4, 376000.0].
"""

half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]

for item in half_lives:
    print(item, end='   ')

    if half_lives[-1] == item:
        print()

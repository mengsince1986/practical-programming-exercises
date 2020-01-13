"""
11. Using a loop, sum the numbers in the range 2 to 22 (inclusive), and then
calculate the average.
"""

total = 0
average = 0
my_range = range(2, 23)

for i in my_range:
    total += i
    if i == 22:
        average = total / len(my_range)

"""
7. Variables population and land_area refer to floats.

a. Write an if statement that will print the population if it is less than 10,000,000.

b. Write an if statement that will print the population if it is between 10,000,000 and 35,000,000.

c. Write an if statement that will print “Densely populated”
if the land density (number of people per unit of area) is greater than 100.

d. Write an if statement that will print “Densely populated”
if the land density (number of people per unit of area) is greater than 100,
and “Sparsely populated” otherwise.
"""

population = 3400000.0
land_area = 10000.0

# a
if population < 10000000:
    print(population)

# b
if 10000000 < population < 35000000:
    print(population)

# c
if (population / land_area) > 100:
    print('Densely populated')

# d
if (population / land_area) > 100:
    print('Densely populated')
else:
    print('Sparsely populated')

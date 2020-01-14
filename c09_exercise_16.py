"""
16. Variables rat_1_weight and rat_2_weight contain the weights of two rats at
the beginning of an experiment. Variables rat_1_rate and rat_2_rate are the rate
that the rats’ weights are expected to increase each week (for example, 4
percent per week).
"""

# a. Using a while loop, calculate how many weeks it would take for the weight
# of the first rat to become 25 percent heavier than it was originally.

rat_1_weight = 1
rat_1_rate = 0.04

rat_2_weight = 1
rat_2_rate = 0.02

weeks = 0

while rat_1_weight < 1 * 1.25:
    rat_1_weight *= 1 + rat_1_rate
    weeks += 1

print(weeks)

# b. Assume that the two rats have the same initial weight, but rat 1 is
# expected to gain weight at a faster rate than rat 2. Using a while loop,
# calculate how many weeks it would take for rat 1 to be 10 percent heavier than
# rat 2.

rat_1_weight = 1
rat_1_rate = 0.04

rat_2_weight = 1
rat_2_rate = 0.02

weeks = 0

while (rat_1_weight - rat_2_weight) / rat_2_weight < 0.1:
    rat_1_weight *= 1 + rat_1_rate
    rat_2_weight *= 1 + rat_2_rate
    weeks += 1

print(weeks)

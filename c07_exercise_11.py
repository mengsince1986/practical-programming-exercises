"""
11. Using string methods, write expressions that produce the following:

a. A copy of 'boolean' capitalized
b. The first occurrence of '2' in 'CO2 H2O'
c. The second occurrence of '2' in 'CO2 H2O'
d. True if and only if 'Boolean' begins lowercase
e. A copy of "MoNDaY" converted to lowercase and then capitalized
f. A copy of " Monday" with the leading whitespace removed
"""

# a
print('boolean'.upper())

# b
print('CO2 H2O'.find('2'))

# c
print('CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1))

# d
print('Boolean'.startswith('Boolean'[0].lower()))

# e
print("MoNDaY".lower().upper())

# f
print(" Monday".lstrip())

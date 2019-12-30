"""
11. Repeat the previous exercise using negative indices.
"""

units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

# a. The first item of units (the first inner list)
print(units[-2])

# b. The last item of units (the last inner list)
print(units[-1])

# c. The string 'km'
print(units[-2][-3])

# d. The string 'kg'
print(units[-1][-3])

# e. The list ['miles', 'league']
print(units[-2][-2:])

# f. The list ['kg', 'pound']
print(units[-1][-3:-1])

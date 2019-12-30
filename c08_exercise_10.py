"""
10. Variable units refers to the nested list

>>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

Using units and either slicing or indexing with positive indices, write
expressions that produce the following:
"""

units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

# a. The first item of units (the first inner list)
print(units[0])

# b. The last item of units (the last inner list)
print(units[1])

# c. The string 'km'
print(units[0][0])

# d. The string 'kg'
print(units[1][0])

# e. The list ['miles', 'league']
print(units[0][1:])

# f. The list ['kg', 'pound']
print(units[1][0:2])

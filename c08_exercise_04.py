"""
4. Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900]. Using
list methods, do the following:
"""

ids = [4353, 2314, 2956, 3382, 9362, 3900]

# a. Remove 3382 from the list.
ids.remove(3382)
print(ids)

# b. Get the index of 9362.
print(ids.index(9362))

# c. Insert 4499 in the list after 9362.
ids.insert(ids.index(9362) + 1, 4499)
print(ids)

# d. Extend the list by adding [5566, 1830] to it.
ids.extend([5566, 1830])
print(ids)

# e. Reverse the list.
ids.reverse()
print(ids)

#f. Sort the list.
ids.sort()
print(ids)

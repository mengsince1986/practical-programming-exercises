"""
6. In this exercise, you’ll create a list and then answer questions about that
list.
"""
# a. Create a list of temperatures in degrees Celsius with the values 25.2,
# 16.8, 31.4, 23.9, 28, 22.5, and 19.6, and assign it to a variable called
# temps.
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]

# b. Using one of the list methods, sort temps in ascending order.
temps.sort()
print(temps)

# c. Using slicing, create two new lists, cool_temps and warm_temps, which
# contain the temperatures below and above 20 degrees Celsius, respectively.
cool_temps = temps[0:2]
print(cool_temps)

warm_temps = temps[2:]
print(warm_temps)

# d. Using list arithmetic, recombine cool_temps and warm_temps into a new list
# called temps_in_celsius.
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

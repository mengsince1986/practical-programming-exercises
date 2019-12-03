"""
1. What value does each expression produce? Verify your answers by typing the expressions into Python.

a. True and not False

b. True and not false (Notice the capitalization.)

c. True or True and False

d. not True or not False

e. True and not 0

f. 52 < 52.3

g. 1 + 52 < 52.3

h. 4 != 4.0
"""

print('True and not False')
print(True and not False)
# True

#print('True and not false')
#print(True and not false)
# Error - name 'false' is not defined

print('True or True and False')
print(True or True and False)
# True
# Boolean operators precedenc order:
# not > and > or

print('not True or not False')
print(not True or not False)
# True

print('True and not 0')
print(True and not 0)
# True

print('52 < 52.3')
print(52 < 52.3)
# True

print('1 + 52 < 52.3')
print(1 + 52 < 52.3)
# False

print('4 != 4.0')
print(4 != 4.0)
# False

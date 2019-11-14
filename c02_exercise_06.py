# 6. Write a bullet list description of what happens when Python evaluates the statement x += x - x when x has the value 3.

x = 3

print('>>> x = 3')

x += x - x

print('>>> x += x - x')

print('* Evaluate x - x on the right of the = sign to produce 0\
      \n* Apply + operator to x which refers to 3 and 0 and produce 3\
      \n* Store the memory address of 3 in variable x')

print('>>> x')

print(x)

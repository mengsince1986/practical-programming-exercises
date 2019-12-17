"""
8. Variable fruit refers to 'pineapple'. For the following function calls,
in what order are the subexpressions evaluated?

a. fruit.find('p', fruit.count('p'))

answer:
1. fruit = 'pineapple'
2. 'p'
3. fruit.count('p')
    4. fruit = 'pineapple'
    5. 'p'
    6. count

b. fruit.count(fruit.upper().swapcase())

answer:
1. fruit = 'pineapple'
2. fruit.upper().swapcase()
    3. fruit = 'pineapple'
    4. upper()
    5. swapcase()

c. fruit.replace(fruit.swapcase(), fruit.lower())

answer:
1. fruit = 'pineapple'
2. fruit.swapcase()
    3. fruit = 'pineapple'
    4. swapcase()
5. fruit.lower()
    6. fruit = 'pineapple'
    7. lower()
"""

"""
11. Why does the last example in Remembering Results of a Boolean
Expression Evaluation, on page 92,

>>> young = age < 45
>>> slim = bmi < 22.0

>>> if young and slim:
        risk = 'low'
    elif young and not slim:
        risk = 'medium'
    elif not young and slim:
        risk = 'medium'
    elif not young and not slim:
        risk = 'high'

check to see whether someone is light (that is, that person’s BMI is
less than the threshold) rather than heavy? If you wanted to write
the second assignment statement as heavy = bmi >= 22.0,
what change(s) would you have to make to the code?
"""

"""
answer: the code checks to see whether someone is light rather than heavy
because it's clearer to reflect the decision table.
"""

# modify the second assignment statement as heavy

age = 33
bmi = 23

young = age < 45
heavy = bmi >= 22.0

if young and heavy:
    risk = 'medium'
elif young and not heavy:
    risk = 'low'
elif not young and heavy:
    risk = 'high'
elif not young and not heavy:
    risk = 'medium'

print(risk)

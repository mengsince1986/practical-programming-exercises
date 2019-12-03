"""
10. The following code displays a message(s) about the acidity of a solution:

>>> ph = float(input("Enter the ph level: "))
>>> if ph < 7.0:
        print("It's acidic!")
    elif ph < 4.0:
        print("It's a strong acid!")

a. What message(s) are displayed when the user enters 6.4?

answer: It's acidic!

b. What message(s) are displayed when the user enters 3.6?

answer: It's acidic!

c. Make a small change to one line of the code so that both messages
are displayed when a value less than 4 is entered.
"""
ph = float(input("Enter the ph level: "))

if ph < 7.0:
    print("It's acidic!")

if ph < 4.0:
    print("It's a strong acid!")

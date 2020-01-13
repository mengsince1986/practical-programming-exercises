"""
8. You are given two lists, rat_1 and rat_2, that contain the daily weights of
two rats over a period of ten days. Assume the rats never have exactly the same
weight. Write statements to do the following:
"""

rat_1 = [8.3, 8.8, 9.0]

rat_2 = [8.2, 8.3, 9.6]

# a. If the weight of rat 1 is greater than that of rat 2 on day 1, print "Rat
# 1 weighed more than rat 2 on day 1."; otherwise, print "Rat 1 weighed less
# than rat 2 on day 1.".

# b. If rat 1 weighed more than rat 2 on day 1 and if rat 1 weighs more than
# rat 2 on the last day, print "Rat 1 remained heavier than Rat 2."; otherwise,
# print "Rat 2 became heavier than Rat 1."

# c. If your solution to the previous exercise used nested if statements, then
# do it without nesting, or vice versa.

# nested version

if rat_1[0] > rat_2[0]:
    print('Rat 1 weighed more than rat 2 on day 1.')

    if rat_1[-1] > rat_2[-1]:
        print('Rat 1 remained heavier than Rat 2.')
    else:
        print('Rat 2 became heavier than Rat 1')
else:
    print('Rat 1 weighted less than rat 2 on day 1.')

## Non-nested version

if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
    print('Rat 1 weighed more than rat 2 on day 1.\nRat 1 remained heavier than\
 Rat 2.')
elif rat_1[0] > rat_2[0] and rat_1[-1] < rat_2[-1]:
    print('Rat 1 wighed more than rat 2 on day 1.\nRat 2 became heavier than\
 Rat 1.')
else:
    print('Rat 1 weighted less than rat 2 on day 1.')

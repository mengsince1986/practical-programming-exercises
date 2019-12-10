"""
2. In the following exercises, you will work with Python’s calendar module:

a. Visit the Python documentation website at
http://docs.python.org/release/3.6.0/py-modindex.html, and look at the
documentation on module calendar.

b. Import module calendar.

c. Using function help, read the description of function isleap.

d. Use isleap to determine the next leap year.

e. Use dir to get a list of what calendar contains.

f. Find and use a function in module calendar to determine how many leap years
there will be between the years 2000 and 2050, inclusive.

g. Find and use a function in module calendar to determine which day of the
week July 29, 2016, will be.
"""

#b
import calendar

#c
# help(calendar.isleap)

#d
def next_leap_year(this_year):
    """(int) -> int
    return the next leap year since this_year

    >>>next_leap_year(2019)
    2020
    >>>next_leap_year(2020)
    2024
    """
    next_year = this_year + 1

    if calendar.isleap(next_year):
        return next_year

    return next_leap_year(next_year)

print('The next leap year since 2019 is', next_leap_year(2019))

#e
# dir(calendar)

#f
def count_leap_years(year_1, year_2):
    """Precondition: year_2 >= year_1

    (int, int) -> int

    return how many leap years between year_1 and year_2, inclusive

    >>> count_leap_years(2020, 2023)
    1
    >>> count_leap_years(2020, 2020)
    1
    >>> count_leap_years(2018, 2028)
    3
    """
    exclusive_leap_years = calendar.leapdays(year_1, year_2)

    if calendar.isleap(year_2):
        return 1 + exclusive_leap_years

    return exclusive_leap_years

print('There are', count_leap_years(2000, 2050),
      'leap years between 2000 and 2050.')

#g
def en_week_day(year, month, day):
    """Precondition: 1 <= month <= 12
                     1 <= day <= 31

    (int, int, int) -> str

    return the day(Monday, Tuesday, ... , Sunday)of the week

    >>> en_week_day(2019, 12, 10)
    'Tuesday'
    """
    week_day = calendar.weekday(year, month, day)

    en_weekday = ''

    if week_day == 0:
        en_weekday = 'Monday'
    elif week_day == 1:
        en_weekday = 'Tuesday'
    elif week_day == 2:
        en_weekday = 'Wednesday'
    elif week_day == 3:
        en_weekday = 'Thursday'
    elif week_day == 4:
        en_weekday = 'Friday'
    elif week_day == 5:
        en_weekday = 'Saturday'
    elif week_day == 6:
        en_weekday = 'Sunday'

    return en_weekday

print('July 29, 2016 is', en_week_day(2016, 7, 29))

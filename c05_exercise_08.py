"""
8. Function convert_to_celsius from Defining Our Own Functions,
on page 35, converts from Fahrenheit to Celsius.
Wikipedia, however, discusses eight temperature scales:
Kelvin, Celsius, Fahrenheit, Rankine,
Delisle, Newton, Rèaumur, and Rømer.
Visit http://en.wikipedia.org/wiki/Comparison_of_temperature_scales
to read about them.

a. Write a convert_temperatures(t, source, target) function
to convert temperature t from source units to target units,
where source and target are each one of "Kelvin", "Celsius",
"Fahrenheit", "Rankine", "Delisle", "Newton", "Reaumur",
and "Romer" units.

Hint: On the Wikipedia page there are eight tables, each with two
columns and seven rows. That translates to an awful lot of if statements
—at least 8 * 7 —because each of the eight units
can be converted to the seven other units.
Possibly even worse, if you decided to add another temperature scale,
you would need to add at least sixteen more if statements:
eight to convert from your new scale to each of the current ones
and eight to convert from the current ones to your new scale.

A better way is to choose one canonical scale, such as Celsius.
Your conversion function could work in two steps:
convert from the source scale to Celsius and
then from Celsius to the target scale.

b. Now if you added a new temperature scale, how many if statements
would you need to add?
"""

# a

def convert_temperatures(t, source, target):
    """(number, str, str) -> number

    convert temperature t from source units to target units, where source and target are each one of
    "Fahrenheit",
    "Kelvin",
    "Celsius",
    "Rankine",
    "Delisle",
    "Newton",
    "Reaumur",
    and "Romer" units.

    >>> convert_temperatures(310, 'kelvin', 'celsius')
    36.85
    >>> convert_temperatures(37, 'celsius', 'fahrenheit')
    98.6
    >>> convert_temperatures(98, 'fahrenheit', 'rankine')
    557.67
    >>> convert_temperatures(558, 'rankine', 'delisle')
    94.725
    >>> convert_temperatures(95, 'delisle', 'newton')
    12.1
    >>> convert_temperatures(12, 'newton', 'reaumur')
    29.09
    >>> convert_temperatures(29, 'reaumur', 'romer')
    26.53125
    """
    # convert source units into celsius units
    if source == 'celsius':
        t = t
    elif source == 'fahrenheit':
        t = (t - 32) * 5 / 9
    elif source == 'kelvin':
        t = t - 273.15
    elif source == 'rankine':
        t = (t - 491.67) * 5 / 9
    elif source == 'delisle':
        t = 100 - t * 2 / 3
    elif source == 'newton':
        t = t * 100 / 33
    elif source == 'reaumur':
        t = t * 5 / 4
    elif source == 'romer':
        t = (t - 7.5) * 40 / 21
    else:
        return 'can not evaluate source'

    # convert celsius units to target units
    if target == 'celsius':
        return t
    elif target == 'fahrenheit':
        return t * 9 / 5 + 32
    elif target == 'kelvin':
        return t + 273.15
    elif target == 'rankine':
        return (t + 273.15) * 9 / 5
    elif target == 'delisle':
        return (100 - t) * 3 / 2
    elif target == 'newton':
        return t * 33 / 100
    elif target == 'reaumur':
        return t * 4 / 5
    elif target == 'romer':
        return t * 21 / 40 + 7.5
    else:
        return 'can not evaluate taget'

"""
b. If adding a new temperature scale, two elif clauses are to be added to the function.
"""

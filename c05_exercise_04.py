"""
4. You want an automatic wildlife camera to switch on if the light level is less than 0.01 lux or if the temperature is above freezing, but not if both conditions are true. (You should assume that function turn_camera_on has already been defined.)

Your first attempt to write this is as follows:

>>> if (light < 0.01) or (temperature > 0.0):
        if not ((light < 0.01) and (temperature > 0.0)):
            turn_camera_on()

A friend says that this is an exclusive or and that you could write it more simply as follows:

>>> if (light < 0.01) != (temperature > 0.0):
        turn_camera_on()

Is your friend right? If so, explain why. If not, give values for light and temperature that will produce different results for the two fragments of code.
"""

light = 0.05
temperature = -9.0

turn_camera_on():
    print("camera on")

"""
The friend is right.

According to the requirements for the camera, there are two conditions:

>>> light < 0.01
>>> temperature > 0.0

And iff one of them is true, the camera is turned on. So it's a typical exclusive or conditions and the firend's solution is dry and right.
"""

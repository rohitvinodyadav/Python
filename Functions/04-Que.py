#  Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circleStats(r):
    area = math.floor(math.pi * r * r)
    circumference = math.floor(2 * math.pi * r)
    return area, circumference

a,c = circleStats(3)
print("Area:", a)
print("Circumference:", c)
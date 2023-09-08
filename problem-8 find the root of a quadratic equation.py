"""
Problem 8: Find the root of a quadratic Equation

"""
import math


a = 2
b = -5
c = 3

# Applying D = b²-4ac
d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("X1 = ", x1, " And X2 = ", x2)

elif d == 0:
    x = (-b) / (2 * a)
    print("X = ", x)

else:
    print(" Root are imaginary")

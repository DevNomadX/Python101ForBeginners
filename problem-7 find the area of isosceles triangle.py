"""
Problem 7: find the area of isosceles triangle with condition

"""

a = 10
b = 11
c = 15

if (a + b) > c and (b + c) > a and (c + a) > b:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(area)

else:
    print("Sorry triangle isn't possible")

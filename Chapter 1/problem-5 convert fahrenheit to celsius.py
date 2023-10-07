"""
Problem 5: Get Fahrenheit Temp from Keyboard And Convert into Celsius

"""

f = float(input("Enter Fahrenheit Value: "))
celsius = (f - 32) * 5 / 9

print(celsius)


# Best Practice
"""def convert(f):
    celsius = (f - 32) * 5 / 9

    return celsius


f = float(input("Enter Fahrenheit Value: "))

if __name__ == "__main__":
    print(convert(f), "Celsius")"""

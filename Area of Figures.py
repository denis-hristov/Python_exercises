shape = input()
a = float(input())

if shape == "square":
    print(a * a)
elif shape == "rectangle":
    b = float(input())
    print(a * b)
elif shape == "circle":
    from math import pi
    print(pi * a * a)
else:
    b = float(input())
    print(a * b / 2)


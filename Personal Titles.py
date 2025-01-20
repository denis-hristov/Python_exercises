age = float(input())
jender = input()

if jender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif jender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

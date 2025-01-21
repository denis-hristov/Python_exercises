food = input()
day = input()
number = float(input())

cost = 0.0

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if food == "banana":
        cost = number * 2.5
    elif food == "apple":
        cost = number * 1.2
    elif food == "orange":
        cost = number * 0.85
    elif food == "grapefruit":
        cost = number * 1.45
    elif food == "kiwi":
        cost = number * 2.7
    elif food == "pineapple":
        cost = number * 5.5
    elif food == "grapes":
        cost = number * 3.85
    else:
        cost = 0.0
elif day in ["Saturday", "Sunday"]:
    if food == "banana":
        cost = number * 2.7
    elif food == "apple":
        cost = number * 1.25
    elif food == "orange":
        cost = number * 0.9
    elif food == "grapefruit":
        cost = number * 1.6
    elif food == "kiwi":
        cost = number * 3
    elif food == "pineapple":
        cost = number * 5.6
    elif food == "grapes":
        cost = number * 4.2
    else:
        cost = 0.0

if cost != 0.0:
    print(f"{cost:.2f}")
else:
    print("error")

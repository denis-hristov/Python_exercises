city = input()
number = float(input())

cost = 0.0

if city == "Sofia":
    if 0 <= number <= 500:
        cost = number * 0.05
    elif number <= 1000:
        cost = number * 0.07
    elif number <= 10000:
        cost = number * 0.08
    elif number > 10000:
        cost = number * 0.12
    else:
        cost = 0.0
elif city == "Varna":
    if 0 <= number <= 500:
        cost = number * 0.045
    elif number <= 1000:
        cost = number * 0.075
    elif number <= 10000:
        cost = number * 0.1
    elif number > 10000:
        cost = number * 0.13
    else:
        cost = 0.0
elif city == "Plovdiv":
    if 0 <= number <= 500:
        cost = number * 0.055
    elif number <= 1000:
        cost = number * 0.08
    elif number <= 10000:
        cost = number * 0.12
    elif number > 10000:
        cost = number * 0.145
    else:
        cost = 0.0

if cost <= 0.0 or number < 0:
    print("error")
else:
    print(f"{cost:.2f}")

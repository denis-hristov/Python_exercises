number = float(input())
day = input()

if 10 <= number <= 18 and day in ["Mondey", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    print("open")
else:
    print("closed")

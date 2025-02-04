name = input()
points = float(input())
number = int(input())

for _ in range(number):
    name1 = input()
    more_points = float(input())

    points += (len(name1) * more_points / 2)

    if points >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        exit()

print(f"Sorry, {name} you need {1250.5 - points:.1f} more!")

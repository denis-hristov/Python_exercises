number = int(input())
points = int(input())
begin_p = points
wins = 0

for _ in range(number):
    result = input()

    if result == "W":
        wins += 1
        points += 2000
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720

print(f"Final points: {points}")
print(f"Average points: {int((points - begin_p) / number)}")
print(f"{(wins / number * 100):.2f}%")

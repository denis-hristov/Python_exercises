width = int(input())
height = int(input())
cake = width * height

while cake >= 0:
    piece = input()
    if piece == "STOP":
        break
    cake -= int(piece)

if cake >= 0:
    print(f"{cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake)} pieces more.")

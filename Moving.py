width = int(input())
length = int(input())
height = int(input())

area = width * length * height

while area > 0:
    box = input()
    if box == "Done":
        break
    area -= int(box)

if area > 0:
    print(f"{area} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(area)} Cubic meters more.")

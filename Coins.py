money = round(float(input()) * 100)
count = 0

while money > 0:
    count += 1
    if money >= 200:
        money -= 200
    elif money >= 100:
        money -= 100
    elif money >= 50:
        money -= 50
    elif money >= 20:
        money -= 20
    elif money >= 10:
        money -= 10
    elif money >= 5:
        money -= 5
    elif money >= 2:
        money -= 2
    elif money >= 1:
        money -= 1

print(count)

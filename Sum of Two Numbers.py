x1 = int(input())
xMax = int(input())
n = int(input())

N = 0
found = False

for i in range(x1, xMax + 1):
    for y in range(x1, xMax + 1):
        N += 1
        if i + y == n:
            found = True
            print(f"Combination N:{N} ({i} + {y} = {n})")
            exit()

if not found:
    print(f"{N} combinations - neither equals {n}")

level = int(input())
apartment = int(input())
flor = level % 2 == 0

for l in range(level, 0, -1):
    matrix = ""

    for a in range(apartment):
        if l == level:
            matrix += f"L{l}{a} "
        elif flor:
            matrix += f"O{l}{a} "
        else:
            matrix += f"A{l}{a} "

    print(matrix.strip())
    flor = not flor

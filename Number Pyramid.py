n = int(input())
line = 1
bigger = False

for t in range(1, n + 1):
    print_line = ""
    for i in range(1, t + 1):
        if line > n:
            bigger = True
            break
        print_line += str(line) + " "
        line += 1
    print(print_line.strip())
    if bigger:
        break

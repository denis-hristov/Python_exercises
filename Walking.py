steps = 0

while steps < 10000:
    command = input()
    
    if command == "Going home":
        steps += int(input())
        break

    steps += int(command)

if steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps - 10000} steps over the goal!")
else:
    print(f"{10000 - steps} more steps to reach goal.")

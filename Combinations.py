n = int(input())
sum_combinations = 0

for i in range(n + 1):
    for y in range(n + 1):
        for t in range(n + 1):
            if i + y + t == n:
                sum_combinations += 1

print(sum_combinations)

begin = int(input())
end = int(input())
result = ""

for i in range(begin, end + 1):
    current = str(i)
    odd_sum = 0
    even_sum = 0

    for t in range(len(current)):
        digit = int(current[t])
        if t % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if odd_sum == even_sum:
        result += f"{i} "

print(result)

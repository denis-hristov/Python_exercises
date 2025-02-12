n = int(input())
result = ""

for number in range(1111, 10000):
    str_number = str(number)
    if '0' in str_number:
        continue

    count = 0
    if n % (number % 10) == 0:
        count += 1
    if n % ((number // 10) % 10) == 0:
        count += 1
    if n % ((number // 100) % 10) == 0:
        count += 1
    if n % (number // 1000) == 0:
        count += 1

    if count == 4:
        result += str(number) + " "

print(result)

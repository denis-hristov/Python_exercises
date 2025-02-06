min_number = float('inf')

while True:
    value = input()
    if value == "Stop":
        break
    number = int(value)
    if number < min_number:
        min_number = number

print(min_number)

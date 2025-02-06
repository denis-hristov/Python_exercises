max_number = float('-inf')

while True:
    value = input()
    if value == "Stop":
        break
    number = int(value)
    if number > max_number:
        max_number = number

print(max_number)

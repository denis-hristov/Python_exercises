sum_numbers = 0

while True:
    input_str = input()
    
    if input_str == "NoMoreMoney":
        break

    amount = float(input_str)

    if amount < 0:
        print("Invalid operation!")
        break

    sum_numbers += amount
    print(f"Increase: {amount:.2f}")

print(f"Total: {sum_numbers:.2f}")

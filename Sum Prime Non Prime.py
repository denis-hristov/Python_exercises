simp_sum = 0
no_simp_sum = 0

while True:
    number = input()
    if number == "stop":
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for t in range(2, int(number ** 0.5) + 1):
            if number % t == 0:
                is_prime = False
                break

    if is_prime:
        simp_sum += number
    else:
        no_simp_sum += number

print(f"Sum of all prime numbers is: {simp_sum}")
print(f"Sum of all non prime numbers is: {no_simp_sum}")

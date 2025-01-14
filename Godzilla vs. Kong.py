budget = float(input())
numberPeople = int(input())
priseTag = float(input())

decor = budget * 0.10
clodingPrice = numberPeople * priseTag

if numberPeople > 150:
    clodingPrice -= clodingPrice * 0.10

sum = decor + clodingPrice
diff = abs(budget - sum)

if sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

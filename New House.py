tipe = input()
pieces = int(input())
budget = float(input())
cost=0.0

if tipe == "Roses":
    cost = pieces * 5
elif tipe == "Dahlias":
    cost = pieces * 3.8
elif tipe == "Tulips":
    cost = pieces * 2.8
elif tipe == "Narcissus":
    cost = pieces * 3
elif tipe == "Gladiolus":
    cost = pieces * 2.5

if pieces > 80 and tipe == "Roses":
    cost *= 0.9
elif pieces > 90 and tipe == "Dahlias":
    cost *= 0.85
elif pieces > 80 and tipe == "Tulips":
    cost *= 0.85
elif pieces < 120 and tipe == "Narcissus":
    cost *= 1.15
elif pieces < 80 and tipe == "Gladiolus":
    cost *= 1.2

if cost <= budget:
    print(f"Hey, you have a great garden with {pieces} {tipe} and {(budget-cost):.2f} leva left.")
else:
    print(f"Not enough money, you need {(cost - budget):.2f} leva more.")

budget = float(input())
season = input()
number = int(input())
cost=0.0

if season == "Summer" or season == "Autumn":
    cost = 4200
elif season == "Spring":
    cost = 3000
elif season == "Winter":
    cost = 2600

if number <= 6:
    cost *= 0.9
elif number <= 11:
    cost *= 0.85
elif number >= 12:
    cost *= 0.75

if number % 2 == 0 and season != "Autumn":
    cost *= 0.95

if cost <= budget:
    print(f"Yes! You have {(budget-cost):.2f} leva left.")
else:
    print(f"Not enough money! You need {(cost-budget):.2f} leva.")

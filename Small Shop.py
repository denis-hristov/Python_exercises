drink = input()
city = input()
number = float(input())

cost = 0.0
if city == "Sofia":
    if drink == "coffee":
        cost = number*0.5
    elif drink == "water":
        cost = number*0.8
    elif drink == "beer":
        cost = number*1.2
    elif drink == "sweets":
        cost = number*1.45
    elif drink == "peanuts":
        cost = number*1.6

elif city == "Plovdiv":
    if drink == "coffee":
        cost = number*0.4
    elif drink == "water":
        cost = number*0.7
    elif drink == "beer":
        cost = number*1.15
    elif drink == "sweets":
        cost = number*1.3
    elif drink == "peanuts":
        cost = number*1.5

elif city == "Varna":
    if drink == "coffee":
        cost = number*0.45
    elif drink == "water":
        cost = number*0.7
    elif drink == "beer":
        cost = number*1.1
    elif drink == "sweets":
        cost = number*1.35
    elif drink == "peanuts":
        cost = number*1.55

print(cost)

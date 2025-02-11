while True:
    city = input()
    if city == "End":
        break

    cost = float(input())
    sum_money = 0

    while sum_money < cost:
        sum_money += float(input())

    print(f"Going to {city}!")

needed_money = float(input())
sum_money = float(input())

days = 0
spend_days = 0
stop = False

while sum_money < needed_money:
    action = input()
    amount = float(input())
    days += 1

    if action == "spend":
        spend_days += 1
        sum_money -= amount
        if sum_money < 0:
            sum_money = 0
        if spend_days == 5:
            stop = True
            break
    else:
        spend_days = 0
        sum_money += amount

if stop:
    print("You can't save the money.")
    print(days)
else:
    print(f"You saved the money for {days} days.")

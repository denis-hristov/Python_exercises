age = int(input())
cost = float(input())
price = int(input())
year = bool(True)
sum = 0.0
toys = 0
money = 0

for i in range(1, age+1, 1):
    if year:
        toys += 1
        year = False
    else:
        money += 10
        sum += money
        sum -= 1
        year = True
sum += (toys * price)       
if cost <= sum:
    print(f"Yes! {(sum - cost):.2f}")
else:
    print(f"No! {(cost - sum):.2f}")

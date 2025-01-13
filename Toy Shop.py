tripPrice = float(input())
puzzles = float(input())
dolls = float(input())
bears = float(input())
minions = float(input())
trucks = float(input())

profit = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
toys = puzzles+dolls+bears+minions+trucks

if toys >= 50:
    profit*=0.75

profit*=0.9

if tripPrice <= profit:
    print(f"Yes! {(profit-tripPrice):.2f} lv left.")
else:
    print(f"Not enough money! {(tripPrice-profit):.2f} lv needed.")




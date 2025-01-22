tipe = input()
row = float(input())
column = float(input())

cost = 0.0

if tipe == "Premiere":
    cost = row * column * 12
elif tipe == "Normal":
    cost = row * column * 7.5
elif tipe == "Discount":
    cost = row * column * 5

print(f"{cost:.2f} leva")

days = int(input())
room_type = input()
feedback = input()

price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

nights = days - 1
discount = 0

if room_type == "apartment":
    if nights < 10:
        discount = 0.30
    elif 10 <= nights <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif room_type == "president apartment":
    if nights < 10:
        discount = 0.10
    elif 10 <= nights <= 15:
        discount = 0.15
    else:
        discount = 0.20

total_price = price_per_night * nights
total_price -= total_price * discount

if feedback == "positive":
    total_price += total_price * 0.25
elif feedback == "negative":
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")
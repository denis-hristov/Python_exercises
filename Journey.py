budget = float(input())
season = input()
cost = 0.0
destination = ""
activity = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        activity = "Camp"
        cost = budget * 0.3
    elif season == "winter":
        activity = "Hotel"
        cost = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        activity = "Camp"
        cost = budget * 0.4
    elif season == "winter":
        activity = "Hotel"
        cost = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    activity = "Hotel"
    cost = budget * 0.9


print(f"Somewhere in {destination}")
print(f"{activity} - {cost:.2f}")

from math import ceil
series = input()
episotTime = int(input())
breaks = int(input())
lunch = breaks/8
chilTime = breaks/4

neededTime = breaks - (lunch + chilTime)

if neededTime>=episotTime:
    print(f"You have enough time to watch {series} and left with {ceil(neededTime-episotTime)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(episotTime-neededTime)} more minutes.")

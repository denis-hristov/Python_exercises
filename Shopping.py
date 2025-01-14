budget = float(input())
videoCards = int(input())
processorso = int(input())
ram = int(input())

neededBudget = videoCards*250+ processorso*(videoCards*250*0.35)\
               + ram*(videoCards*250*0.1)
if videoCards>processorso:
    neededBudget *= 0.85

if budget>=neededBudget:
    print(f"You have {(abs(neededBudget-budget)):.2f} leva left!")
else:
    print(f"Not enough money! You need {(abs(budget-neededBudget)):.2f} leva more!")

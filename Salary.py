n = int(input())
salary = int(input())

for i in range(1, n+1, 1):
    media = input()
    if media == "Facebook":
        salary -= 150
    elif media == "Instagram":
        salary -= 100
    elif media == "Reddit":
        salary -= 50
if salary>0:
    print(salary)
else:
    print("You have lost your salary.")

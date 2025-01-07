lenght = int(input())
width = int(input())
hight = int(input())
procentage = float(input())/100

sum = lenght * width * hight
sum_liters = sum * 0.001

used_liters = sum_liters - sum_liters*procentage
print(used_liters)
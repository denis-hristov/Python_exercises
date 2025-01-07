a = int(input())
b = int(input())
c = int(input())
master = int(input())

nylons = (a + 2) * 1.5
paint = (b + b*0.1) * 14.5
organizer = c * 5.0
bags = 0.4

sum = nylons+paint+organizer+bags
discount_and_master = (sum * 0.3) * master

print(sum + discount_and_master)

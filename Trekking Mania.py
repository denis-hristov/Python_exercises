number = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
sum_numbers = 0

for _ in range(number):
    new_number = int(input())
    sum_numbers += new_number

    if new_number <= 5:
        p1 += new_number
    elif new_number <= 12:
        p2 += new_number
    elif new_number <= 25:
        p3 += new_number
    elif new_number <= 40:
        p4 += new_number
    elif new_number >= 41:
        p5 += new_number

print(f"{(p1 / sum_numbers * 100):.2f}%")
print(f"{(p2 / sum_numbers * 100):.2f}%")
print(f"{(p3 / sum_numbers * 100):.2f}%")
print(f"{(p4 / sum_numbers * 100):.2f}%")
print(f"{(p5 / sum_numbers * 100):.2f}%")

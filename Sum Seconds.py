a = int(input())
b = int(input())
c = int(input())

sum = a+b+c

min = sum//60
sec = sum%60

print(f"{min}:{sec:02d}")


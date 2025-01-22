a = int(input())
b = int(input())
symbol = input()
result = ""

if symbol == '+':
    sum = a + b
    result = "even" if sum % 2 == 0 else "odd"
    print(f"{a} {symbol} {b} = {sum} - {result}")
elif symbol == '-':
    sum = a - b
    result = "even" if sum % 2 == 0 else "odd"
    print(f"{a} {symbol} {b} = {sum} - {result}")
elif symbol == '*':
    sum = a * b
    result = "even" if sum % 2 == 0 else "odd"
    print(f"{a} {symbol} {b} = {sum} - {result}")
elif symbol == '/':
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        division = a / b
        print(f"{a} {symbol} {b} = {division:.2f}")
elif symbol == '%':
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        sum = a % b
        print(f"{a} {symbol} {b} = {sum}")

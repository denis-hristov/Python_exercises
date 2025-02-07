name = input()
count = 0
found = False

while True:
    book = input()
    if book == "No More Books":
        break
    if book == name:
        found = True
        break
    count += 1

if found:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")

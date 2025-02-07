name = input()
grade = 1
bad_grades = 0
total_grades = 0
count_grades = 0

while grade <= 12:
    current_grade = float(input())

    if current_grade < 4:
        bad_grades += 1
        if bad_grades == 2:
            print(f"{name} has been excluded at {grade} grade")
            break
        continue

    total_grades += current_grade
    count_grades += 1
    grade += 1
else:
    print(f"{name} graduated. Average grade: {total_grades / count_grades:.2f}")

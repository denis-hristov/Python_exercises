poor_grades_limit = int(input())
poor_grades_count = 0
exercises = 0
total_score = 0
last_problem = ""
needs_break = False

while True:
    problem_name = input()
    if problem_name == "Enough":
        break

    grade = int(input())
    total_score += grade
    exercises += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count == poor_grades_limit:
            needs_break = True
            break

if needs_break:
    print(f"You need a break, {poor_grades_count} poor grades.")
else:
    print(f"Average score: {total_score / exercises:.2f}")
    print(f"Number of problems: {exercises}")
    print(f"Last problem: {last_problem}")

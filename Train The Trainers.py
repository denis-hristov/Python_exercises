judges = int(input())
end_print = ""
end_sum = 0
projects = 0

while True:
    name = input()
    if name == "Finish":
        break

    sum_scores = 0
    for _ in range(judges):
        sum_scores += float(input())

    end_print += f"{name} - {(sum_scores / judges):.2f}.\n"
    end_sum += sum_scores / judges
    projects += 1

print(f"{end_print}Student's final assessment is {(end_sum / projects):.2f}.")

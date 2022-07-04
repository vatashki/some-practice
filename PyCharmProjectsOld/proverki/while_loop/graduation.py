name = input()
mark = float(input())

grade = 1
counter = 0
student_in_school = True
total_mark = 0

while student_in_school:
    if mark >= 4:
        total_mark += mark
        grade += 1
        mark = float(input())
        if grade == 12:
            student_in_school = False
            total_mark += mark
    else:
        counter += 1
        if counter > 1:
            student_in_school = False


mean_mark = total_mark / grade

if grade == 12:
    print(f"{name} graduated. Average grade: {mean_mark:.2f}")
elif grade < 12:
    print(f"{name} has been excluded at {grade} grade")
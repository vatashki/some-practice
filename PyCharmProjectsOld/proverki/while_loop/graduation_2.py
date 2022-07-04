name = input()

year = 1
total_mark = 0
counter = 0

while year <= 12:
    mark = float(input())
    if mark >= 4:
        year += 1
        total_mark += mark
    else:
        counter += 1
        if counter > 1:
            break

mean_mark = total_mark / year

if year == 12:
    print(f"{name} graduated. Average grade: {mean_mark:.2f}")
else:
    print(f"{name} has been excluded at {year} grade")
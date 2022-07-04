hour = int(input())
day = input()

working_hours = hour >= 10 and hour <= 18
working_days = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"

if working_hours and working_days:
    print("open")
else:
    print("closed")


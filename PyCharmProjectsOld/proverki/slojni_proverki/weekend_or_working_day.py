day = input()

# working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"
# weekend = day == "Saturday" or day == "Sunday"

# if working_day:
#    print('Working day')
# elif weekend:
#    print(Weekend)
# else:
#    print('Error')

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")
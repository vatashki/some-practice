day = input()

twelve = day == "Monday" or day == "Tuesday" or day == "Friday"
fourteen = day == "Wednesday" or day == "Thursday"
sixteen = day == "Saturday" or day == "Sunday"

if twelve:
    print("12")
elif fourteen:
    print("14")
elif sixteen:
    print("16")
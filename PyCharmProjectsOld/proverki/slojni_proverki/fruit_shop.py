fruit = input()
day = input()
amount = float(input())

week_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"
weekend = day == "Saturday" or day == "Sunday"

if week_day:
    if fruit == "banana":
        price = 2.50
        print(f"{price * amount:.2f}")
    elif fruit == "apple":
        price = 1.20
        print(f"{price * amount:.2f}")
    elif fruit == "orange":
        price = 0.85
        print(f"{price * amount:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        print(f"{price * amount:.2f}")
    elif fruit == "kiwi":
        price = 2.70
        print(f"{price * amount:.2f}")
    elif fruit == "pineapple":
        price = 5.50
        print(f"{price * amount:.2f}")
    elif fruit == "grapes":
        price = 3.85
        print(f"{price * amount:.2f}")
    else:
        print("error")
elif weekend:
    if fruit == "banana":
        price = 2.70
        print(f"{price * amount:.2f}")
    elif fruit == "apple":
        price = 1.25
        print(f"{price * amount:.2f}")
    elif fruit == "orange":
        price = 0.90
        print(f"{price * amount:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        print(f"{price * amount:.2f}")
    elif fruit == "kiwi":
        price = 3.00
        print(f"{price * amount:.2f}")
    elif fruit == "pineapple":
        price = 5.60
        print(f"{price * amount:.2f}")
    elif fruit == "grapes":
        price = 4.20
        print(f"{price * amount:.2f}")
    else:
        print("error")
else:
    print("error")

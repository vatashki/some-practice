city = input()
revenue = float(input())

commission = 0
revenue_range_1 = revenue >= 0 and revenue <= 500
revenue_range_2 = revenue > 500 and revenue <= 1000
revenue_range_3 = revenue > 1000 and revenue <= 10000
revenue_range_4 = revenue > 10000

if city == "Sofia" and revenue_range_1:
    commission = 0.05
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Sofia" and revenue_range_2:
    commission = 0.07
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Sofia" and revenue_range_3:
    commission = 0.08
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Sofia" and revenue_range_4:
    commission = 0.12
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Varna" and revenue_range_1:
    commission = 0.045
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Varna" and revenue_range_2:
    commission = 0.075
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Varna" and revenue_range_3:
    commission = 0.1
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Varna" and revenue_range_4:
    commission = 0.13
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Plovdiv" and revenue_range_1:
    commission = 0.055
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Plovdiv" and revenue_range_2:
    commission = 0.08
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Plovdiv" and revenue_range_3:
    commission = 0.12
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
elif city == "Plovdiv" and revenue_range_4:
    commission = 0.145
    commission_amount = f"{commission * revenue:.2f}"
    print(commission_amount)
else:
    print("error")

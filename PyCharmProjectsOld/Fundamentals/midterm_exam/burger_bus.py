number_of_cities = int(input())

total_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    if city % 3 == 0 and city % 5 != 0:
        current_profit = income - expenses * 1.5
        total_profit += current_profit
        print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")
    elif city % 5 == 0:
        current_profit = income * 0.9 - expenses
        total_profit += current_profit
        print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")
    else:
        current_profit = income - expenses
        total_profit += current_profit
        print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")


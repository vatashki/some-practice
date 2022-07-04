film_budget = float(input())
extras_amount = int(input())
price_per_clothing = float(input())

decor_price = 0.1 * film_budget

total_clothing_price = extras_amount * price_per_clothing

if extras_amount > 150:
    final_price = (total_clothing_price - total_clothing_price * 0.1) + decor_price
    if final_price <= film_budget:
        money_left = film_budget - final_price
        print("Action!")
        print(f"Wingard starts filming with {money_left:.2f} leva left.")
    else:
        money_needed = final_price - film_budget
        print("Not enough money!")
        print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    final_price = total_clothing_price + decor_price
    if final_price <= film_budget:
        money_left = film_budget - final_price
        print("Action!")
        print(f"Wingard starts filming with {money_left:.2f} leva left.")
    else:
        money_needed = final_price - film_budget
        print("Not enough money!")
        print(f"Wingard needs {money_needed:.2f} leva more.")
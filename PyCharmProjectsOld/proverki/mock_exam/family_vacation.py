budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_spendings = int(input())

price_for_stay = number_of_nights * price_per_night
additional_spendings_amount = budget * percent_additional_spendings / 100

if number_of_nights > 7:
    price_for_stay = price_for_stay - (price_for_stay * 0.05)

total_spendings = price_for_stay + additional_spendings_amount

money_difference = abs(total_spendings - budget)

if total_spendings <= budget:
    print(f"Ivanovi will be left with {money_difference:.2f} leva after vacation.")
else:
    print(f"{money_difference:.2f} leva needed.")


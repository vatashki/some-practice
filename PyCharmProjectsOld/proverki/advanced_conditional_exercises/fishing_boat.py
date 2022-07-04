budget = int(input())
season = input()
number_of_fishermen = int(input())

ship_price = 0
discount = 0
additional_discount = 0
price_with_discount = 0
final_price = 0

if season == "Spring":
    ship_price = 3000
    if number_of_fishermen <= 6:
        discount = ship_price * 0.1
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
    elif 7 <= number_of_fishermen <= 11:
        discount = ship_price * 0.15
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
    elif 12 <= number_of_fishermen:
        discount = ship_price * 0.25
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
    if number_of_fishermen <= 6:
        discount = ship_price * 0.1
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0 and season == "Summer":
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
    elif 7 <= number_of_fishermen <= 11:
        discount = ship_price * 0.15
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
    elif 12 <= number_of_fishermen:
        discount = ship_price * 0.25
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
elif season == "Winter":
    ship_price = 2600
    if number_of_fishermen <= 6:
        discount = ship_price * 0.1
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
    elif 7 <= number_of_fishermen <= 11:
        discount = ship_price * 0.15
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount
    elif 12 <= number_of_fishermen:
        discount = ship_price * 0.25
        price_with_discount = ship_price - discount
        if number_of_fishermen % 2 == 0:
            additional_discount = price_with_discount * 0.05
            final_price = price_with_discount - additional_discount
        else:
            final_price = price_with_discount

money_difference = abs(budget - final_price)
money_difference_formatted = f"{money_difference:.2f}"

if budget >= final_price:
    print(f"Yes! You have {money_difference_formatted} leva left.")
else:
    print(f"Not enough money! You need {money_difference_formatted} leva.")

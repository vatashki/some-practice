price_luggage_over_20_kg = float(input())
luggage_kg = float(input())
days_to_travel = int(input())
pieces_of_luggage = int(input())

total_price = 0
price_per_luggage = 0

if luggage_kg > 20:
    price_per_luggage = price_luggage_over_20_kg
    if days_to_travel > 30:
        total_price = (price_per_luggage + (price_per_luggage * 0.1)) * pieces_of_luggage
    elif 7 <= days_to_travel <= 30:
        total_price = (price_per_luggage + (price_per_luggage * 0.15)) * pieces_of_luggage
    else:
        total_price = (price_per_luggage + (price_per_luggage * 0.4)) * pieces_of_luggage
elif 10 <= luggage_kg <= 20:
    price_per_luggage = price_luggage_over_20_kg * 0.5
    if days_to_travel > 30:
        total_price = (price_per_luggage + (price_per_luggage * 0.1)) * pieces_of_luggage
    elif 7 <= days_to_travel <= 30:
        total_price = (price_per_luggage + (price_per_luggage * 0.15)) * pieces_of_luggage
    else:
        total_price = (price_per_luggage + (price_per_luggage * 0.4)) * pieces_of_luggage
else:
    price_per_luggage = price_luggage_over_20_kg * 0.2
    if days_to_travel > 30:
        total_price = (price_per_luggage + (price_per_luggage * 0.1)) * pieces_of_luggage
    elif 7 <= days_to_travel <= 30:
        total_price = (price_per_luggage + (price_per_luggage * 0.15)) * pieces_of_luggage
    else:
        total_price = (price_per_luggage + (price_per_luggage * 0.4)) * pieces_of_luggage

print(f"The total price of bags is: {total_price:.2f} lv.")

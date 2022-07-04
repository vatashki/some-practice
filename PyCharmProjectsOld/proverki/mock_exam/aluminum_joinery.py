number_of_joinery = int(input())
type_of_joinery = input()
delivery = input()

price_per_joinery = 0

if type_of_joinery == "90X130":
    price_per_joinery = 110
    if 60 > number_of_joinery >= 30:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.05)
    elif number_of_joinery >= 60:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.08)
elif type_of_joinery == "100X150":
    price_per_joinery = 140
    if 80 > number_of_joinery >= 40:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.06)
    elif number_of_joinery >= 80:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.1)
elif type_of_joinery == "130X180":
    price_per_joinery = 190
    if 50 > number_of_joinery >= 20:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.07)
    elif number_of_joinery >= 50:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.12)
elif type_of_joinery == "200X300":
    price_per_joinery = 250
    if 50 > number_of_joinery >= 25:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.09)
    elif number_of_joinery >= 50:
        price_per_joinery = price_per_joinery - (price_per_joinery * 0.14)

total_price = number_of_joinery * price_per_joinery
final_price = 0
final_final_price = 0

if delivery == "With delivery":
    final_price = total_price + 60
elif delivery == "Without delivery":
    final_price = total_price

if number_of_joinery < 10:
    print("Invalid order")
elif number_of_joinery > 99:
    final_final_price = final_price - (final_price * 0.04)
    print(f"{final_final_price:.2f} BGN")
else:
    final_final_price = final_price
    print(f"{final_final_price:.2f} BGN")

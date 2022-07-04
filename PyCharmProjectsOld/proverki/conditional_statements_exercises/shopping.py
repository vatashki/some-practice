budget = float(input())
video_amount = int(input())
processor_amount = int(input())
ram_amount = int(input())

video_price = 250
total_video_price = video_price * video_amount

processor_price = total_video_price * 0.35
ram_price = total_video_price * 0.1

total_processor_price = processor_price * processor_amount
total_ram_price = ram_price* ram_amount

total_price = total_video_price \
    + total_processor_price \
    + total_ram_price

total_price_with_discount = total_price - total_price * 0.15

if video_amount > processor_amount:
    if budget >= total_price_with_discount:
        money_left = budget - total_price_with_discount
        print(f"You have {money_left:.2f} leva left!")
    else:
        money_needed = total_price_with_discount - budget
        print(f"Not enough money! You need {money_needed:.2f} leva more!")
else:
    if budget >= total_price:
        money_left = budget - total_price
        print(f"You have {money_left:.2f} leva left!")
    else:
        money_needed = total_price - budget
        print(f"Not enough money! You need {money_needed:.2f} leva more!")
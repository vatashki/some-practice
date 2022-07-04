flower_type = input()
flower_amount = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

total_price = 0
final_price = 0

if flower_type == "Roses":
    total_price = rose_price * flower_amount
    if flower_amount > 80:
        final_price = total_price - total_price * 0.1
    else:
        final_price = total_price
elif flower_type == "Dahlias":
    total_price = dahlia_price * flower_amount
    if flower_amount > 90:
        final_price = total_price - total_price * 0.15
    else:
        final_price = total_price
elif flower_type == "Tulips":
    total_price = tulip_price * flower_amount
    if flower_amount > 80:
        final_price = total_price - total_price * 0.15
    else:
        final_price = total_price
elif flower_type == "Narcissus":
    total_price = narcissus_price * flower_amount
    if flower_amount < 120:
        final_price = total_price + total_price * 0.15
    else:
        final_price = total_price
elif flower_type == "Gladiolus":
    total_price = gladiolus_price * flower_amount
    if flower_amount < 80:
        final_price = total_price + total_price * 0.2
    else:
        final_price = total_price

sum_difference = abs(budget - final_price)
sum_difference = f"{sum_difference:.2f}"

if budget >= final_price:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {sum_difference} leva left.")
else:
    print(f"Not enough money, you need {sum_difference} leva more.")
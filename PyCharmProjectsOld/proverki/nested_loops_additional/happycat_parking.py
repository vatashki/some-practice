number_of_days = int(input())
hours_per_day = int(input())

total_price_counter = 0

for day in range(1, number_of_days + 1):
    price_per_day = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 ==0 and hour % 2 != 0:
            total_price_counter += 2.50
            price_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            total_price_counter += 1.25
            price_per_day += 1.25
        else:
            total_price_counter += 1
            price_per_day += 1
        if hour == hours_per_day:
            print(f"Day: {day} - {price_per_day:.2f} leva")

print(f"Total: {total_price_counter:.2f} leva")


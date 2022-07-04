age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

money_present = 0
toy_present = 0
total_money = 0
money_from_toys = 0

for number in range(1, age + 1):
    if number % 2 != 0:
        toy_present += 1
    else:
        money_present = money_present + 10
        total_money = total_money + money_present - 1

money_from_toys = toy_present * price_per_toy

final_money = total_money + money_from_toys

money_difference = abs(final_money - washing_machine_price)

if final_money >= washing_machine_price:
    print(f"Yes! {money_difference:.2f}")
else:
    print(f"No! {money_difference:.2f}")
pocket_money = float(input())
money_per_day = float(input())
all_expenses = float(input())
gift_price = float(input())

final_money = (pocket_money * 5) + (money_per_day * 5) - all_expenses

difference = abs(final_money - gift_price)

if final_money >= gift_price:
    print(f"Profit: {final_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {difference:.2f} BGN.")

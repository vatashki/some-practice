strawberries_price = float(input())
bananas_amount = float(input())
oranges_amount = float(input())
raspberries_amount = float(input())
strawberries_amount = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

total_strawberries_price = strawberries_price * strawberries_amount
total_bananas_price = bananas_price * bananas_amount
total_oranges_price = oranges_price * oranges_amount
total_raspberries_price = raspberries_price * raspberries_amount

final_price = total_strawberries_price\
            + total_raspberries_price\
            + total_oranges_price\
            + total_bananas_price

print(f"{final_price:.2f}")

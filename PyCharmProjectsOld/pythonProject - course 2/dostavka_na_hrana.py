chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
delivery_price = 2.50

chicken_amount = int(input())
fish_amount = int(input())
vegetarian_amount = int(input())

final_chicken_price = chicken_price * chicken_amount
final_fish_price = fish_price * fish_amount
final_vegetarian_price = vegetarian_price * vegetarian_amount

total_price = final_chicken_price + final_fish_price + final_vegetarian_price
dessert_price = 0.2 * total_price

final_price = total_price + dessert_price + delivery_price

print(final_price)
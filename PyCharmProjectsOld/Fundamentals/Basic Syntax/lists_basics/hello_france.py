items_list = input().split('|')
budget = float(input())

original_budget = budget

max_price_clothes = 50.00
max_price_shoes = 35.00
max_price_accessories = 20.50

bought_items = []

for item in items_list:
    type_and_price = item.split('->')
    if type_and_price[0] == 'Clothes' and float(type_and_price[1]) <= max_price_clothes:
        if budget >= float(type_and_price[1]):
            budget -= float(type_and_price[1])
            bought_items.append(item)
    if type_and_price[0] == 'Shoes' and float(type_and_price[1]) <= max_price_shoes:
        if budget >= float(type_and_price[1]):
            budget -= float(type_and_price[1])
            bought_items.append(item)
    if type_and_price[0] == 'Accessories' and float(type_and_price[1]) <= max_price_accessories:
        if budget >= float(type_and_price[1]):
            budget -= float(type_and_price[1])
            bought_items.append(item)

new_prices_list = []

for item in bought_items:
    type_and_price = item.split('->')
    income = float(type_and_price[1]) * 1.4
    new_price = f'{float(type_and_price[1]) * 1.4:.2f}'

    new_prices_list.append(new_price)
    budget += income

profit = budget - original_budget

print(' '.join(new_prices_list))
print(f'Profit: {profit:.2f}')
if budget > 150:
    print('Hello, France!')
else:
    print('Not enough money.')


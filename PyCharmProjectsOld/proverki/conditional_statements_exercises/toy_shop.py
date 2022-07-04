vacation_price = float(input())
jigsaw_amount = int(input())
talking_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

jigsaw_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_order_amount = jigsaw_amount \
    + talking_doll_amount \
    + teddy_bear_amount \
    + minion_amount \
    + truck_amount

total_jigsaw_price = jigsaw_price * jigsaw_amount
total_doll_price = talking_doll_price * talking_doll_amount
total_bear_price = teddy_bear_price * teddy_bear_amount
total_minion_price = minion_price * minion_amount
total_truck_price = truck_price * truck_amount

total_price = total_jigsaw_price \
    + total_doll_price \
    + total_bear_price \
    + total_minion_price \
    + total_truck_price

if total_order_amount >= 50:
    final_price = total_price - 0.25 * total_price
    store_rent = 0.1 * final_price
    money_left = final_price - store_rent
    if money_left >= vacation_price:
        money_after_vacation = money_left - vacation_price
        print(f"Yes! {money_after_vacation:.2f} lv left.")
    else:
        money_needed = vacation_price - money_left
        print(f"Not enough money! {money_needed:.2f} lv needed.")
else:
    final_price = total_price
    store_rent = 0.1 * final_price
    money_left = final_price - store_rent
    if money_left >= vacation_price:
        print(f"Yes! {money_left: .2f} lv left.")
    else:
        money_needed = vacation_price - money_left
        print(f"Not enough money! {money_needed:.2f} lv needed.")
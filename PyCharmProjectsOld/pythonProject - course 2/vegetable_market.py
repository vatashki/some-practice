price_kg_vegetables_lv = float(input())
price_kg_fruit_lv = float(input())
amount_of_vegetables = int(input())
amount_of_fruit = int(input())

price_kg_vegetables_eur = price_kg_vegetables_lv / 1.94
price_kg_fruit_eur = price_kg_fruit_lv / 1.94

total_money_vegetables = price_kg_vegetables_eur * amount_of_vegetables
total_money_fruit = price_kg_fruit_eur * amount_of_fruit

final_money = total_money_fruit + total_money_vegetables

formated_final_money = "{:.2f}".format(final_money)

print(formated_final_money)
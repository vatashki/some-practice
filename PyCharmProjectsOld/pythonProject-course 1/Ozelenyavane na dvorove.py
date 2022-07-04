kv_met = float(input())

obshta_cena = kv_met * 7.61
cena_s_namalenie = obshta_cena - (0.18 * obshta_cena)
discount = 18 / 100 * obshta_cena

print(f"The final price is: {cena_s_namalenie} lv.")
print(f"The discount is: {discount} lv.")

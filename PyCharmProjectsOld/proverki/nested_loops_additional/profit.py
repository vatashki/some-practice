lv1_count = int(input())
lv2_count = int(input())
lv5_count = int(input())
money_amount = int(input())

for lv1_amount in range(0, lv1_count + 1):
    for lv2_amount in range(0, lv2_count + 1):
        for lv5_amount in range(0, lv5_count + 1):
            if lv1_amount + lv2_amount * 2 + lv5_amount * 5 == money_amount:
                print(f"{lv1_amount} * 1 lv. + {lv2_amount} * 2 lv. + {lv5_amount} * 5 lv. = {money_amount} lv.")


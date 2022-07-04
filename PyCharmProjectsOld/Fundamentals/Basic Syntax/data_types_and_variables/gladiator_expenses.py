lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# helmet_count = 0
# sword_count = 0
# shield_count = 0
# armor_count = 0
#
# for loss in range(1, lost_fights + 1):
#     if loss % 2 == 0:
#         helmet_count += 1
#     if loss % 3 == 0:
#         sword_count += 1
#         if loss % 2 == 0:
#             shield_count += 1
#             if shield_count % 2 == 0:
#                 armor_count += 1

helmet_count = lost_fights // 2
sword_count = lost_fights // 3
shield_count = lost_fights // 6
armor_count = shield_count // 2

total_helmet_price = helmet_price * helmet_count
total_sword_price = sword_price * sword_count
total_shield_price = shield_price * shield_count
total_armor_price = armor_price * armor_count

total_price = total_helmet_price + total_sword_price + total_shield_price + total_armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")

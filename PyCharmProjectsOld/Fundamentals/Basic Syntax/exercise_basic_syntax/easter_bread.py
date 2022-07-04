budget = float(input())
kg_flour_price = float(input())

pack_of_eggs_price = 0.75 * kg_flour_price
liter_milk_price = 1.25 * kg_flour_price
ml_250_milk_price = liter_milk_price / 4

price_per_loaf = pack_of_eggs_price + kg_flour_price + ml_250_milk_price
loaf_counter = 0
coloured_egg_counter = 0

while budget > price_per_loaf:
    budget -= price_per_loaf
    loaf_counter += 1
    coloured_egg_counter += 3
    if loaf_counter % 3 == 0:
        coloured_egg_counter -= loaf_counter - 2

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {coloured_egg_counter} eggs and {budget:.2f}BGN left.")
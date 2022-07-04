quantity_of_decorations = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

price_counter = 0
points_counter = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        price_counter += ornament_set_price * quantity_of_decorations
        points_counter += ornament_set_points
    if day % 3 == 0:
        price_counter += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        points_counter += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        price_counter += tree_lights_price * quantity_of_decorations
        points_counter += tree_lights_points
    if day % 3 == 0 and day % 5 == 0:
        points_counter += 30
    if day % 10 == 0:
        points_counter -= 20
        price_counter += tree_skirt_price + tree_garland_price + tree_lights_price
    if day % 10 == 0 and day == days_until_christmas:
        points_counter -= 30

print(f"Total cost: {price_counter}")
print(f"Total spirit: {points_counter}")


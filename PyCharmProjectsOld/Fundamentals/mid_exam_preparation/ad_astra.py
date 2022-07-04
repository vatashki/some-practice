food_item = input()

food_item_as_list = []

if "#" in food_item:
    food_item_as_list = food_item.split("#")
elif "|" in food_item:
    food_item_as_list = food_item.split("|")

print(food_item_as_list)

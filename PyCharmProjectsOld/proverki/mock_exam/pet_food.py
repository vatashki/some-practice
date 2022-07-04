number_of_days = int(input())
amount_of_food = float(input())

amount_of_biscuits = 0
amount_of_food_eaten = 0
days_counter = 0
total_dog_food_eaten = 0
total_cat_food_eaten = 0

for days in range(number_of_days):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    total_dog_food_eaten += dog_food_eaten
    total_cat_food_eaten += cat_food_eaten
    days_counter += 1
    amount_of_food_eaten += (dog_food_eaten + cat_food_eaten)
    if days_counter % 3 == 0:
        amount_of_biscuits += 0.1 * (dog_food_eaten + cat_food_eaten)

percent_of_amount_of_food_eaten = amount_of_food_eaten / amount_of_food * 100
dog_food_percent = total_dog_food_eaten / amount_of_food_eaten * 100
cat_food_percent = total_cat_food_eaten / amount_of_food_eaten * 100

print(f"Total eaten biscuits: {round(amount_of_biscuits)}gr.")
print(f"{percent_of_amount_of_food_eaten:.2f}% of the food has been eaten.")
print(f"{dog_food_percent:.2f}% eaten from the dog.")
print(f"{cat_food_percent:.2f}% eaten from the cat.")

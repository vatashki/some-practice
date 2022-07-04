number_of_snowballs = int(input())

highest_points = 0
current_weight = 0
current_time = 0
current_quality = 0

for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_per_snowball = int(input())
    quality_of_snowball = int(input())
    points_per_snowball = (weight_of_snowball / time_per_snowball) ** quality_of_snowball
    if points_per_snowball > highest_points:
        highest_points = points_per_snowball
        current_weight = weight_of_snowball
        current_time = time_per_snowball
        current_quality = quality_of_snowball

print(f"{current_weight} : {current_time} = {int(highest_points)} ({current_quality})")

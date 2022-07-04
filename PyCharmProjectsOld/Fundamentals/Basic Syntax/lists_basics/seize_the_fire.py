fires_list = input().split('#')
water_amount = int(input())
starting_water = water_amount

for fire in fires_list:
    current_fire = fire.split()
    if current_fire[0] == 'High':
        if int(current_fire[2]) < 81 or int(current_fire[2]) > 125:
            fires_list.insert(fire.index(fire), 'Skip')
            fires_list.pop(fires_list.index(fire))
    if current_fire[0] == 'Medium':
        if int(current_fire[2]) < 51 or int(current_fire[2]) > 80:
            fires_list.insert(fire.index(fire), 'Skip')
            fires_list.pop(fires_list.index(fire))
    if current_fire[0] == 'Low':
        if int(current_fire[2]) < 1 or int(current_fire[2]) > 50:
            fires_list.insert(fire.index(fire), 'Skip')
            fires_list.pop(fires_list.index(fire))

total_effort = 0

finished_with_all_fires = False
iteration_counter = 0

while water_amount > 0:
    if finished_with_all_fires:
        break
    for fire in fires_list:
        iteration_counter += 1
        current_fire = fire.split()
        if fire != 'Skip':
            if water_amount >= int(current_fire[2]):
                water_amount -= int(current_fire[2])
                total_effort += 0.25 * int(current_fire[2])
            else:
                fires_list.insert(iteration_counter, 'Skip')
                fires_list.pop(fires_list.index(fire))
        if iteration_counter == len(fires_list):
            finished_with_all_fires = True
        if finished_with_all_fires:
            break

total_fire = starting_water - water_amount

print('Cells:')
for fire_put_out in fires_list:
    if fire_put_out != 'Skip':
        current_fire = fire_put_out.split()
        print(f' - {current_fire[2]}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')

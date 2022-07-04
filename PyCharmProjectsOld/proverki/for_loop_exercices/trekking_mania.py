number_of_groups = int(input())

people_in_group = 0
total_climbers_musala = 0
total_climbers_montblanc = 0
total_climbers_kilimanjaro = 0
total_climbers_k2 = 0
total_climbers_everest = 0

for group in range(number_of_groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        total_climbers_musala += people_in_group
    if 5 < people_in_group <= 12:
        total_climbers_montblanc += people_in_group
    if 12 < people_in_group <= 25:
        total_climbers_kilimanjaro += people_in_group
    if 25 < people_in_group <= 40:
        total_climbers_k2 += people_in_group
    if 40 < people_in_group:
        total_climbers_everest += people_in_group

total_number_of_climbers = total_climbers_musala \
                           + total_climbers_montblanc \
                           + total_climbers_kilimanjaro \
                           + total_climbers_k2 \
                           + total_climbers_everest

musala_percent = total_climbers_musala / total_number_of_climbers * 100
montblanc_percent = total_climbers_montblanc / total_number_of_climbers * 100
kilimanjaro_percent = total_climbers_kilimanjaro / total_number_of_climbers * 100
k2_percent = total_climbers_k2 / total_number_of_climbers * 100
everest_percent = total_climbers_everest / total_number_of_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
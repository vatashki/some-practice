tank_length = int(input())
tank_width = int(input())
tank_hight = int(input())
percent_filled = float(input()) / 100

tank_volume = tank_length * tank_width * tank_hight
tank_volume_liters = tank_volume * 0.001

needed_liters = tank_volume_liters * (1 - percent_filled)

print(needed_liters)
import math

free_days = int(input())
work_days = 365 - free_days
play_norm = 30000

free_days_play = 127 * free_days
work_days_play = 63 * work_days
total_play_time = free_days_play + work_days_play

hours_play = abs(math.floor(total_play_time - play_norm)) // 60
minutes_play = abs(math.floor(total_play_time - play_norm)) % 60

if total_play_time > play_norm:
    print("Tom will run away")
    print(f"{hours_play} hours and {minutes_play} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_play} hours and {minutes_play} minutes less for play")

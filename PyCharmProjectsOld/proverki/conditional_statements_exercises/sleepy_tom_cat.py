import math

free_days = int(input())

work_days = 365 - free_days
play_on_free_days = 127 * free_days
play_on_work_days = 63 * work_days
play_norm = 30000
total_play = play_on_free_days + play_on_work_days

play_needed = play_norm - total_play
play_time_left = total_play - play_norm

hours_play_needed = math.floor(play_needed // 60)
minutes_play_needed = math.floor(play_needed % 60)
hours_play_time_left = math.floor(play_time_left // 60)
minutes_play_time_left = math.floor(play_time_left % 60)

if total_play >= play_norm:
    print("Tom will run away")
    print(f"{hours_play_time_left} hours and {minutes_play_time_left} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_play_needed} hours and {minutes_play_needed} minutes less for play")
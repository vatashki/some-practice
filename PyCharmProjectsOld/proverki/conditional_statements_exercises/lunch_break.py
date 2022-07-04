import math

series_name = str(input())
episode_length = int(input())
break_length = int(input())

lunch_length = 1 / 8 * break_length
rest_length = 1 / 4 * break_length

time_for_episode = break_length - lunch_length - rest_length

time_left = math.ceil(time_for_episode - episode_length)
time_needed = math.ceil(episode_length - time_for_episode)

if time_for_episode >= episode_length:
    print(f"You have enough time to watch {series_name} and left with {time_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {time_needed} more minutes.")
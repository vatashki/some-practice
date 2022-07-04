import math

record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

slow_down_seconds = math.floor(distance_meters / 15) * 12.5

ivans_seconds = distance_meters * seconds_per_meter + slow_down_seconds

time_needed = ivans_seconds - record_seconds

if ivans_seconds > record_seconds:
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {ivans_seconds:.2f} seconds.")
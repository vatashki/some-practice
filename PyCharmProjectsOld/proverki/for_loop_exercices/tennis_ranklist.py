import math

number_of_tournaments = int(input())
starting_points = int(input())
stage_reached = ""

points_from_tournament = 0

number_of_w = 0

for tournament in range(number_of_tournaments):
    stage_reached = input()
    if stage_reached == "W":
        points_from_tournament += 2000
        number_of_w += 1
    if stage_reached == "F":
        points_from_tournament += 1200
    if stage_reached == "SF":
        points_from_tournament += 720

total_points = starting_points + points_from_tournament

average_points = math.floor(points_from_tournament / number_of_tournaments)

percent_tournaments_won = number_of_w / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_tournaments_won:.2f}%")

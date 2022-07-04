import math

number_of_balls = int(input())

points = 0
number_of_red_balls = 0
number_of_orange_balls = 0
number_of_yellow_balls = 0
number_of_white_balls = 0
number_of_black_balls = 0
number_of_other_balls = 0

for i in range(number_of_balls):
    colour_of_ball = input()
    if colour_of_ball == "red":
        points += 5
        number_of_red_balls += 1
    elif colour_of_ball == "orange":
        points += 10
        number_of_orange_balls += 1
    elif colour_of_ball == "yellow":
        points += 15
        number_of_yellow_balls += 1
    elif colour_of_ball == "white":
        points += 20
        number_of_white_balls += 1
    elif colour_of_ball == "black":
        points /= 2
        points = math.floor(points)
        number_of_black_balls += 1
    else:
        number_of_other_balls += 1
        continue

print(f"Total points: {points}")
print(f"Red balls: {number_of_red_balls}")
print(f"Orange balls: {number_of_orange_balls}")
print(f"Yellow balls: {number_of_yellow_balls}")
print(f"White balls: {number_of_white_balls}")
print(f"Other colors picked: {number_of_other_balls}")
print(f"Divides from black balls: {number_of_black_balls}")
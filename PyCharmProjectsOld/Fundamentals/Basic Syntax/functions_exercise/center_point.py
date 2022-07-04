import math


def point_closest_to_the_center(x1, y1, x2, y2):
    point_one_sum = abs(x1) + abs(y1)
    point_two_sum = abs(x2) + abs(y2)
    if point_one_sum <= point_two_sum:
        return math.floor(x1), math.floor(y1)
    elif point_one_sum > point_two_sum:
        return math.floor(x2), math.floor(y2)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print(point_closest_to_the_center(x_1, y_1, x_2, y_2))

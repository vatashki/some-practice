import math

shape_type = input()


if shape_type == "square":
    side_length = float(input())
    square_area = side_length ** 2
    print(f"{square_area:.3f}")
elif shape_type == "rectangle":
    side_a_length = float(input())
    side_b_length = float(input())
    rectangle_area = side_b_length * side_a_length
    print(f"{rectangle_area:.3f}")
elif shape_type == "circle":
    radius = float(input())
    circle_area = math.pi * radius ** 2
    print(f"{circle_area:.3f}")
elif shape_type == "triangle":
    triangle_side = float(input())
    hight = float(input())
    triangle_area = triangle_side * hight / 2
    print(f"{triangle_area:.3f}")
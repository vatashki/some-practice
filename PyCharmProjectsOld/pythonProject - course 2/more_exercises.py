import math

b1 = float(input())
b2 = float(input())
h = float(input())

trapezoid_area = (b1 + b2) * h / 2

formted_area = "{:.2f}".format(trapezoid_area)
print(formted_area)

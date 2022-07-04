x_house_hight = float(input())
y_house_length = float(input())
h_roof_hight = float(input())

door = 1.2 * 2
window = 1.5 * 1.5
front_wall = x_house_hight * x_house_hight - door
back_wall = x_house_hight * x_house_hight
side_wall = x_house_hight * y_house_length - window
roof_side = x_house_hight * y_house_length
roof_front = 0.5 * x_house_hight * h_roof_hight

house_area = front_wall + back_wall + side_wall * 2
roof_area = roof_side * 2 + roof_front * 2

green_paint = house_area / 3.4
red_paint = roof_area / 4.3

formated_green_paint = "{:.2f}".format(green_paint)
formated_red_paint = "{:.2f}".format(red_paint)

print(formated_green_paint)
print(formated_red_paint)

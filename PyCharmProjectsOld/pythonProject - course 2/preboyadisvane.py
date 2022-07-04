square_meters_nylon_cover = int(input())
paint_liters = int(input())
paint_thinner = int(input())
work_hours = int(input())

added_paint_amount = 10/100 * paint_liters
added_square_meters_nylon_cover = 2
bag_price = 0.40


price_paint = (paint_liters + added_paint_amount) * 14.50
price_nylon_cover = (square_meters_nylon_cover + added_square_meters_nylon_cover) * 1.50
price_paint_thinner = paint_thinner * 5.00

work_price = 30/100 * (price_paint + price_paint_thinner + price_nylon_cover + bag_price) * work_hours

total_price = bag_price +\
    price_nylon_cover +\
    price_paint +\
    price_paint_thinner +\
    work_price

print(total_price)
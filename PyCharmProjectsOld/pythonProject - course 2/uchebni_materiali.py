pen_packages = int(input())
marker_packages = int(input())
board_cleaner_liters = int(input())
price_reduction_percent = int(input())

total_pen_price = pen_packages * 5.80
total_markers_price = marker_packages * 7.20
total_board_cleaner_price = board_cleaner_liters * 1.20

price_reduction = (total_pen_price + \
                   total_markers_price + \
                   total_board_cleaner_price) * price_reduction_percent / 100

final_price = total_pen_price + total_markers_price + total_board_cleaner_price - price_reduction

print(final_price)

last_sector = input()
rows_in_1st_sector = int(input())
odd_row_seats = int(input())

first_sector = "A"

first_sector_integer = ord(first_sector)
last_sector_integer = ord(last_sector)

first_seat = "a"
first_seat_integer = ord(first_seat)

sector_counter = 65                     # 65 = "A"
number_of_rows = rows_in_1st_sector

even_row_seats = odd_row_seats + 2
last_seat_even = first_seat_integer + even_row_seats
last_seat_odd = first_seat_integer + odd_row_seats

seat_counter = 0

for sector in range(first_sector_integer, last_sector_integer + 1):
    if sector_counter > first_sector_integer:
        number_of_rows += 1
    for row in range(1, number_of_rows + 1):
        sector_counter += 1
        if row % 2 != 0:
            for seat in range(first_seat_integer, last_seat_odd):
                print(f"{chr(sector)}{row}{chr(seat)}")
                seat_counter += 1
        if row % 2 == 0:
            for seat in range(first_seat_integer, last_seat_even):
                print(f"{chr(sector)}{row}{chr(seat)}")
                seat_counter += 1

print(seat_counter)

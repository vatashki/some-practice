showing_type = input()
r_rows = int(input())
c_columns = int(input())

price = 0

if showing_type == "Premiere":
    price = 12.00
elif showing_type == "Normal":
    price = 7.50
elif showing_type == "Discount":
    price = 5.00

revenue = price * r_rows * c_columns

print(f"{revenue:.2f} leva")

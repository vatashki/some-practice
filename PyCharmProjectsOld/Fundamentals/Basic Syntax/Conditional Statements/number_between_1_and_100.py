number_between_1_100 = False

number = 0

while not number_between_1_100:
    number = float(input())
    if 1 > number > 100:
        continue
    if 1 <= number <= 100:
        number_between_1_100 = True

if number_between_1_100:
    print(f"The number {number} is between 1 and 100")


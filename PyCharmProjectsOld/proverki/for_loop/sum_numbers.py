numbers_amount = int(input())

digits = 0

for number in range(0, numbers_amount):
    numbers = int(input())
    digits += numbers

print(digits)
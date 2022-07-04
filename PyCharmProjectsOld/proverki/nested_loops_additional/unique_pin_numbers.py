number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

for first_number in range(1, number_1 + 1):
    for second_number in range(1, number_2 + 1):
        for third_number in range(1, number_3 + 1):
            if first_number % 2 == 0 and (second_number == 2 or second_number == 3 or second_number == 5 or second_number ==  7) and third_number % 2 == 0:
                print(f"{first_number} {second_number} {third_number}")


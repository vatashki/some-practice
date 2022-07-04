k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0

for first_number_first_digit in range(k, 8 + 1):
    for first_number_second_digit in range(9, l - 1, -1):
        for second_number_first_digit in range(m, 8 + 1):
            for second_number_second_digit in range(9, n - 1, -1):
                if first_number_first_digit % 2 == 0 and first_number_second_digit % 2 != 0 and second_number_first_digit % 2 == 0 and second_number_second_digit % 2 != 0:
                    if counter == 6:
                        break
                    if first_number_first_digit != second_number_first_digit or first_number_second_digit != second_number_second_digit:
                        counter += 1
                        print(f"{first_number_first_digit}{first_number_second_digit} - {second_number_first_digit}{second_number_second_digit}")
                    else:
                        print("Cannot change the same player.")

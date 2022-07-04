number_input = input()

number_first_digit = int(number_input[2])
number_second_digit = int(number_input[1])
number_third_digit = int(number_input[0])

for number_1 in range(1, number_first_digit + 1):
    for number_2 in range(1, number_second_digit + 1):
        for number_3 in range(1, number_third_digit + 1):
            multiplied = number_1 * number_2 * number_3
            print(f"{number_1} * {number_2} * {number_3} = {multiplied};")
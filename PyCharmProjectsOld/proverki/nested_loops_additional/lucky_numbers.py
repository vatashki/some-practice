number_n = int(input())

for number_1 in range(1, number_n + 1):
    for number_2 in range(1, number_n + 1):
        for number_3 in range(1, number_n + 1):
            for number_4 in range(1, number_n + 1):
                if (number_1 + number_2) != (number_3 + number_4):
                    continue
                if number_n % (number_1 + number_2) != 0:
                    continue
                print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")

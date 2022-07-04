number_of_letters = int(input())

for symbol_1 in range(97, 97 + number_of_letters):
    for symbol_2 in range(97, 97 + number_of_letters):
        for symbol_3 in range(97, 97 + number_of_letters):
            print(f"{chr(symbol_1)}{chr(symbol_2)}{chr(symbol_3)}")

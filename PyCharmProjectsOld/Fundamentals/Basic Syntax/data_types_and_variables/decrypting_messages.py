key = int(input())
number_of_symbols = int(input())

for symbol in range(number_of_symbols):
    current_symbol = input()
    decrypted_symbol = key + ord(current_symbol)
    print(chr(decrypted_symbol), end='')

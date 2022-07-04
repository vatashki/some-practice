starting_symbol = int(input())
ending_symbol = int(input())
#
# for symbol in range(starting_symbol, ending_symbol + 1):
#     print(chr(symbol), end=' ')

final_string = ''

for symbol in range(starting_symbol, ending_symbol + 1):
    final_string += chr(symbol) + ' '

print(final_string)
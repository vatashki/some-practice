number_of_lines = int(input())

total_sum = 0

for symbols in range(number_of_lines):
    symbol = input()
    total_sum += ord(symbol)

print(f"The sum equals: {total_sum}")

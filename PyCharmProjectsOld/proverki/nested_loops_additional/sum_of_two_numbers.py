start = int(input())
end = int(input())
magic_number = int(input())

equals_magic_number = False
combination_counter = 0

for num_1 in range(start, end + 1):
    if equals_magic_number:
        break
    for num_2 in range(start, end + 1):
        combination_counter += 1
        sum_of_numbers = num_1 + num_2
        if sum_of_numbers == magic_number:
            print(f"Combination N:{combination_counter} ({num_1} + {num_2} = {magic_number})")
            equals_magic_number = True
            break

if equals_magic_number == False:
    print(f"{combination_counter} combinations - neither equals {magic_number}")

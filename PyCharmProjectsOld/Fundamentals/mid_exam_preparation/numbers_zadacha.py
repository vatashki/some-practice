numbers_list = [int(x) for x in input().split()]

sorted_reversed_numbers = sorted(numbers_list, reverse=True)

average_value = sum(sorted_reversed_numbers) / len(sorted_reversed_numbers)

larger_than_average = []

iteration_counter = 0

for number in sorted_reversed_numbers:
    if iteration_counter <= 4:
        if number > average_value:
            numbers_list.remove(number)
            larger_than_average.append(number)
        iteration_counter += 1

final_list = [str(x) for x in larger_than_average]

if len(larger_than_average) > 0:
    print(" ".join(final_list))
else:
    print("No")


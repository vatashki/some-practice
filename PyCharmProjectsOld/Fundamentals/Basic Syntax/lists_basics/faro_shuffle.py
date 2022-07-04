start_combination = input()
number_of_shuffles = int(input())

previous_shuffle = start_combination.split()
current_shuffle = []

middle_of_combination = int(len(previous_shuffle)/2)

first_half = []
second_half = []

for combination in range(1, number_of_shuffles + 1):
    first_half = previous_shuffle[:middle_of_combination]
    second_half = previous_shuffle[middle_of_combination:]
    for number_in_current_shuffle in range(int(len(previous_shuffle) / 2)):
        current_shuffle.append(first_half[number_in_current_shuffle])
        current_shuffle.append(second_half[number_in_current_shuffle])
    if len(current_shuffle) == len(previous_shuffle):
        previous_shuffle = current_shuffle
    if combination != number_of_shuffles:
        current_shuffle = []
    else:
        break

print(current_shuffle)

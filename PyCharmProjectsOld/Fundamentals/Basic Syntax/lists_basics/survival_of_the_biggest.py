string_of_integers = input().split()
amount_to_remove = int(input())

list_of_integers = [int(x) for x in string_of_integers]

for num in range(amount_to_remove):
    list_of_integers.remove(min(list_of_integers))

iteration_counter = 0

for number in list_of_integers:
    if iteration_counter < len(list_of_integers) - 1:
        print(number, end=", ")
    else:
        print(number)
    iteration_counter += 1

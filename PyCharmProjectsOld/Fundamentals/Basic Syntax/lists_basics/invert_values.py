string_of_numbers = input()

string_to_list_of_strings = string_of_numbers.split()
list_of_integers = [int(x) for x in string_to_list_of_strings]
list_to_print = []

for number in range(len(list_of_integers)):
    if list_of_integers[number] > 0:
        list_to_print.append(-abs(list_of_integers[number]))
    else:
        list_to_print.append(abs(list_of_integers[number]))

print(list_to_print)

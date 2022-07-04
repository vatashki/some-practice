def collapse(some_list, some_command):
    numbers_as_integers_list = [int(x) for x in some_list]
    numbers_sequence_final = []
    while any(x < int(some_command[1]) for x in numbers_as_integers_list):
        numbers_as_integers_list.remove(min(numbers_as_integers_list))
        numbers_sequence_final = [str(y) for y in numbers_as_integers_list]
    return numbers_sequence_final


sequence_of_numbers = input().split()

command = input()
while command != "Finish":
    list_of_commands = command.split()
    if list_of_commands[0] == "Add":
        sequence_of_numbers.append(list_of_commands[1])
    elif list_of_commands[0] == "Remove":
        sequence_of_numbers.remove(list_of_commands[1])
    elif list_of_commands[0] == "Replace":
        for number in range(len(sequence_of_numbers)):
            if sequence_of_numbers[number] == list_of_commands[1]:
                sequence_of_numbers[number] = list_of_commands[2]
                break
    elif list_of_commands[0] == "Collapse":
        sequence_of_numbers = collapse(sequence_of_numbers, list_of_commands)
    command = input()

print(" ".join(sequence_of_numbers))
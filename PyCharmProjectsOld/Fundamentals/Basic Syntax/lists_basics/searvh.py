number_of_strings = int(input())
word = input()

list_of_strings = []

for string in range(number_of_strings):
    current_string = input()
    list_of_strings += [current_string]

print(list_of_strings)

for item_in_list in range(len(list_of_strings) -1, -1, -1):
    element = list_of_strings[item_in_list]
    if word not in element:
        list_of_strings.remove(element)

print(list_of_strings)

first_string = input()
second_string = input()

current_string = ''
transformed_string = ''

for char in range(1, len(first_string) + 1):
    if char == 1:
        current_string = first_string
    transformed_string = second_string[:char:] + first_string[char::]
    if transformed_string != current_string:
        print(transformed_string)
    current_string = transformed_string


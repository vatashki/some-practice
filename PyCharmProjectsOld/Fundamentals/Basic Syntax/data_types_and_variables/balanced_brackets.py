number_of_lines = int(input())

string_to_check = ''

for line in range(number_of_lines):
    current_line = input()
    if current_line == '(' or current_line == ')':
        string_to_check += current_line

string_to_check_comparison = ''

if len(string_to_check) % 2 == 0:
    for check in range(1, len(string_to_check) + 1):
        if check % 2 != 0:
            string_to_check_comparison += '('
        if check % 2 == 0:
            string_to_check_comparison += ')'
else:
    for check in range(1, len(string_to_check) + 2):
        if check % 2 == 1:
            string_to_check_comparison += '('
        if check % 2 == 0:
            string_to_check_comparison += ')'

if string_to_check == string_to_check_comparison:
    print('BALANCED')
else:
    print('UNBALANCED')


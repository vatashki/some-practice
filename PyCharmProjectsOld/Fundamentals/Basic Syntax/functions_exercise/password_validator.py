def is_password_valid(a):
    is_correct_length = False
    is_only_letters_and_digits = False
    contains_more_than_2_digits = False
    if 6 <= len(a) <= 10:
        is_correct_length = True
    iteration_counter = 0
    list_with_valid_symbols = []
    for symbol in a:
        iteration_counter += 1
        if 48 <= ord(symbol) <= 57 or 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
            list_with_valid_symbols.append(symbol)
        if len(list_with_valid_symbols) == len(a) and iteration_counter == len(a):
            is_only_letters_and_digits = True
    digit_counter = 0
    for symbol in a:
        if 48 <= ord(symbol) <= 57:
            digit_counter += 1
        if digit_counter >= 2:
            contains_more_than_2_digits = True
            break
    if is_correct_length and is_only_letters_and_digits and contains_more_than_2_digits:
        print('Password is valid')
    else:
        if not is_correct_length:
            print('Password must be between 6 and 10 characters')
        if not is_only_letters_and_digits:
            print('Password must consist only of letters and digits')
        if not contains_more_than_2_digits:
            print('Password must have at least 2 digits')


password = list(input())

is_password_valid(password)
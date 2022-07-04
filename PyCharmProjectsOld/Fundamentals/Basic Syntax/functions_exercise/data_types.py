

def action (string_1, string_2):
    if string_1 == "int":
        new_string_2 = int(string_2) * 2
        return new_string_2
    if string_1 == "real":
        new_string_2 = f"{(float(string_2) * 1.5):.2f}"
        return new_string_2
    if string_1 == "string":
        new_string_2 = "$" + string_2 + "$"
        return new_string_2


first_string = input()
second_string = input()

print(action(first_string, second_string))

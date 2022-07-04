a = int(input())
b = int(input())
maximum_number_passwords = int(input())

A = 35
B = 64

combinations_counter = 1

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        if A > 55:
            A = 35
        B += 1
        if B > 96:
            B = 64
        combinations_counter += 1
        if combinations_counter > maximum_number_passwords:
            break
    if combinations_counter > maximum_number_passwords:
        break

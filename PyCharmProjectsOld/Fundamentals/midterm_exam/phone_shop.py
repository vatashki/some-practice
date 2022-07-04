phones_list = input().split(", ")

command = input().split(" - ")

while command[0] != "End":
    if command[0] == "Add":
        if command[1] not in phones_list:
            phones_list.append(command[1])
    if command[0] == "Remove":
        if command[1] in phones_list:
            phones_list.remove(command[1])
    if command[0] == "Bonus phone":
        both_phones = command[1].split(":")
        if both_phones[0] in phones_list:
            for phone in range(len(phones_list)):
                if phones_list[phone] == both_phones[0]:
                    phones_list.insert(phone + 1, both_phones[1])
    if command[0] == "Last":
        if command[1] in phones_list:
            phones_list.remove(command[1])
            phones_list.append(command[1])
    command = input().split(" - ")

print(", ".join(phones_list))


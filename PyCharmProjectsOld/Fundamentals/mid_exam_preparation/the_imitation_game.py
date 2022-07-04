encrypted_message = input()
encrypted_message_list = list(encrypted_message)

command = input().split("|")

while True:
    if command[0] == "Move":
        for letter in range(int(command[1])):
            encrypted_message_list.append(encrypted_message_list[0])
            encrypted_message_list.pop(0)
    if command[0] == "Insert":
        encrypted_message_list.insert(int(command[1]), command[2])
    if command[0] == "ChangeAll":
        for i in range(len(encrypted_message_list)):
            if encrypted_message_list[i] == command[1]:
                encrypted_message_list[i] = command[2]
    if command[0] == "Decode":
        decrypted_message_string = "".join(encrypted_message_list)
        print(f"The decrypted message is: {decrypted_message_string}")
        break
    command = input().split("|")

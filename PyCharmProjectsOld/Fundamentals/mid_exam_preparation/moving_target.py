targets = [int(x) for x in input().split()]

command = input().split()

while command[0] != "End":
    if command[0] == "Shoot":
        if int(command[1]) < len(targets):
            targets[int(command[1])] -= int(command[2])
            if targets[int(command[1])] == 0:
                targets.pop(int(command[1]))
    if command[0] == "Add":
        if int(command[1]) < len(targets):
            targets.insert(int(command[1]), int(command[2]))
        else:
            print("Invalid placement!")
    if command[0] == "Strike":
        targets_to_remove = int(command[2]) * 2 + 1
        if int(command[1]) - int(command[2]) < 0 or\
                int(command[1]) + int(command[2]) > len(targets):
            print("Strike missed!")
        else:
            for target in range(targets_to_remove):
                targets.pop((int(command[1])) - (int(command[2])))
    command = input().split()

print("|".join([str(x) for x in targets]))


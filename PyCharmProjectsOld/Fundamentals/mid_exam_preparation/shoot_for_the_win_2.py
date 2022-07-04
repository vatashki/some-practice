targets_list = [int(x) for x in input().split()]

command = input()

shot_targets_counter = 0

while command != "End":
    for i in range(len(targets_list)):
        if i == int(command):
            pass
        else:
            if int(command) >= len(targets_list):
                command = input()
                continue
            else:
                if targets_list[i] == -1:
                    command = input()
                    continue
                if targets_list[i] > targets_list[int(command)]:
                    targets_list[i] -= targets_list[int(command)]
                else:
                    targets_list[i] += targets_list[int(command)]
        targets_list[i] = -1
        command = input()

print(targets_list)
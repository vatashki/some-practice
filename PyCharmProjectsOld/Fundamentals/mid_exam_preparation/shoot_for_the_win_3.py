targets_list = [int(x) for x in input().split()]

command = input()

while command != "End":
    command = int(command)
    if command < len(targets_list):
        for i in range(len(targets_list)):
            if i == command:
                continue
            if targets_list[command] < targets_list[i] and targets_list[i] != -1:
                targets_list[i] -= targets_list[command]
            elif targets_list[command] >= targets_list[i] and targets_list[i] != -1:
                targets_list[i] += targets_list[command]
        targets_list[command] = -1
    command = input()

shot_targets_counter = 0

for x in range(len(targets_list)):
    if targets_list[x] == -1:
        shot_targets_counter += 1

targets_list_strings = [str(x) for x in targets_list]

print(f"Shot targets: {shot_targets_counter} -> {' '.join(targets_list_strings)}")

targets_list = [int(x) for x in input().split()]

command = input()

shot_targets_counter = 0

while command != "End":
    if int(command) >= len(targets_list):
        command = input()
        continue
    for i in range(len(targets_list)):
        if targets_list[i] != -1:
            for x in range(len(targets_list)):
                if x != int(command):

                    if targets_list[x] < targets_list[int(command)]:
                        targets_list[x] -= targets_list[int(command)]
                    else:
                        targets_list[x] += targets_list[int(command)]
            targets_list[int(command)] = -1
    command = input()

for x in range(len(targets_list)):
    if x == -1:
        shot_targets_counter += 1

targets_strings = [str(x) for x in targets_list]
unpacked_targets = " ".join(targets_strings)

print(f"Shot targets: {shot_targets_counter} -> {unpacked_targets}")


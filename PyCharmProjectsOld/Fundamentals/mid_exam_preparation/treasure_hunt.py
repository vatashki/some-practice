initial_loot = input().split("|")

command = input().split()

while command != "Yohoho!":
    if command[0] == "Loot":
        new_loot_list = []
        for x in range(len(command)):
            if x != 0:
                new_loot_list.append(command[x])
        for x in range(len(new_loot_list)):
            if new_loot_list[x] not in initial_loot:
                initial_loot.insert(0, new_loot_list[x])
    if command[0] == "Drop":
        if int(command[1]) < len(initial_loot):
            initial_loot.append(initial_loot[int(command[1])])
            initial_loot.pop(int(command[1]))
    if command[0] == "Steal":
        stolen_items_list = []
        if int(command[1]) >= len(initial_loot) - 1:
            for x in range(len(initial_loot)):
                stolen_items_list.append(initial_loot[x])
                initial_loot = []
        else:
            for x in range(int(command[1])):
                stolen_items_list.append(initial_loot[len(initial_loot) - 1])
                initial_loot.pop(len(initial_loot) - 1)
        reversed_stolen_items = reversed(stolen_items_list)
        print(", ".join(reversed_stolen_items))
    command = input().split()
    if command[0] == "Yohoho!":
        break

sum_of_characters = 0
sum_of_treasures = len(initial_loot)

for treasure in range(len(initial_loot)):
    treasure_to_list = list(initial_loot[treasure])
    sum_of_characters += len(treasure_to_list)

average_gain = sum_of_characters / sum_of_treasures

if len(initial_loot) >= 1:
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")


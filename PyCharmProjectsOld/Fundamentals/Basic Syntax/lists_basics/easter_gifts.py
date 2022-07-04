planned_gifts = input().split()

command = input()

while command != 'No Money':
    command_list = command.split()
    if command_list[0] == 'OutOfStock':
        for gift in planned_gifts:
            if gift == command_list[1]:
                planned_gifts.insert(int(planned_gifts.index(command_list[1]) + 1), 'None')
                planned_gifts.remove(command_list[1])
    if command_list[0] == 'Required' and int(command_list[2]) <= len(planned_gifts):
        planned_gifts.insert((int(command_list[2]) + 1), command_list[1])
        planned_gifts.pop(int(command_list[2]))
    if command_list[0] == 'JustInCase':
        planned_gifts.remove(planned_gifts[-1])
        planned_gifts.append(command_list[1])
    command = input()

final_gifts = []

for gift in planned_gifts:
    if gift != 'None':
        final_gifts.append(gift)

print(' '.join(final_gifts))

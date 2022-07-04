people_waiting = int(input())
lift = [int(x) for x in input().split()]

wagon_counter = 0

for wagon in lift:
    people_to_board = 4 - lift[wagon_counter]
    if lift[wagon_counter] < 4 and people_to_board < people_waiting:
        lift[wagon_counter] += people_to_board
        people_waiting -= people_to_board
    elif lift[wagon_counter] < 4 and people_to_board > people_waiting:
        lift[wagon_counter] += people_waiting
        print("The lift has empty spots!")
        print(lift)
        break
    elif lift[wagon_counter] == len(lift) - 1 and lift[wagon_counter] < 4 and people_to_board < people_waiting:
        lift[wagon_counter] += people_to_board
        people_waiting -= people_to_board
        print(f"There isn't enough space! {people_waiting} people in queue!")
        print(lift)
    else:
        print(lift)
    wagon_counter += 1

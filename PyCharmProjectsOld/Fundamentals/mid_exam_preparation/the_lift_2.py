people_waiting = int(input())
lift = [int(x) for x in input().split()]

wagon_counter = 0

for wagon in range(len(lift)):
    if people_waiting >= 4:
        people_to_board = 4 - lift[wagon_counter]
    else:
        people_to_board = people_waiting
    if wagon_counter != len(lift) - 1 and lift[wagon_counter] < 4 and people_waiting > 0:
        lift[wagon_counter] += people_to_board
        people_waiting -= people_to_board
    elif wagon_counter != len(lift) - 1 and lift[wagon_counter] < 4 and people_waiting <= 0:
        print("The lift has empty spots!")
        print(" ".join(str(x) for x in lift))
    elif wagon_counter == len(lift) - 1 and lift[wagon_counter] < 4 and people_waiting > 0 and people_waiting > people_to_board:
        lift[wagon_counter] += people_to_board
        people_waiting -= people_to_board
        print(f"There isn't enough space! {people_waiting} people in a queue!")
        print(" ".join(str(x) for x in lift))
    elif wagon_counter == len(lift) - 1 and lift[wagon_counter] < 4 and people_waiting > 0 and people_waiting == people_to_board:
        lift[wagon_counter] += people_to_board
        people_waiting -= people_to_board
        print("The lift has empty spots!")
        print(" ".join(str(x) for x in lift))
    elif wagon_counter == len(lift) - 1 and lift[wagon_counter] < 4 and people_waiting <= 0:
        print("The lift has empty spots!")
        print(" ".join(str(x) for x in lift))
    elif wagon_counter == len(lift) - 1 and lift[wagon_counter] == 4 and people_waiting > 0 and people_waiting > people_to_board:
        print(f"There isn't enough space! {people_waiting} people in a queue!")
        print(" ".join(str(x) for x in lift))
    elif wagon_counter == len(lift) - 1 and lift[wagon_counter] == 4 and people_waiting > 0 and people_waiting == people_to_board:
        print("The lift has empty spots!")
        print(" ".join(str(x) for x in lift))
    elif wagon_counter == len(lift) - 1 and lift[wagon_counter] == 4 and people_waiting <= 0:
        print(" ".join(str(x) for x in lift))
    wagon_counter += 1

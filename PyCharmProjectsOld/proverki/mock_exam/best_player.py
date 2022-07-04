name_of_player = input()
number_of_goals = int(input())

most_goals = 0
best_player = ""
hat_trick = False

while name_of_player != "END":
    if number_of_goals > most_goals:
        most_goals = number_of_goals
        best_player = name_of_player
        if number_of_goals >= 3:
            hat_trick = True
    if number_of_goals >= 10:
        most_goals = number_of_goals
        best_player = name_of_player
        hat_trick = True
        break
    name_of_player = input()
    if name_of_player == "END":
        break
    number_of_goals = int(input())

print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")

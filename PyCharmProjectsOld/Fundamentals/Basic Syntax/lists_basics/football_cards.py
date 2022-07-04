string_of_players = input()

team_A_list = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_B_list = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

string_to_list_of_strings = string_of_players.split()

game_terminated = False

for player in range(len(string_to_list_of_strings)):
    if len(team_A_list) < 7 or len(team_B_list) < 7:
        game_terminated = True
        break
    if 'A' in string_to_list_of_strings[player]:
        team_A_list.remove(string_to_list_of_strings[player])
    if 'B' in string_to_list_of_strings[player]:
        team_B_list.remove(string_to_list_of_strings[player])

print(f'Team A - {len(team_A_list)}; Team B - {len(team_B_list)}')
if game_terminated:
    print('Game was terminated')


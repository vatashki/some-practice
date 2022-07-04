start_number = int(input())
end_number = int(input())

for character_1 in range(start_number, end_number + 1):
    for character_2 in range(start_number, end_number + 1):
        for character_3 in range(start_number, end_number + 1):
            for character_4 in range(start_number, end_number + 1):
                if (character_1 % 2 == 0) and (character_4 % 2 == 0):
                    continue
                if (character_1 % 2 != 0) and (character_4 % 2 != 0):
                    continue
                if character_1 <= character_4:
                    continue
                if (character_2 + character_3) % 2 != 0:
                    continue
                print(f"{character_1}{character_2}{character_3}{character_4}", end=" ")

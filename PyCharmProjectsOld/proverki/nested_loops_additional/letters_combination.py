letter_1 = input()
letter_2 = input()
letter_3 = input()

character_1 = ord(letter_1)
character_2 = ord(letter_2)
character_3 = ord(letter_3)

counter = 0

for symbol_1 in range(character_1, character_2 + 1):
    for symbol_2 in range(character_1, character_2 + 1):
        for symbol_3 in range(character_1, character_2 + 1):
            if symbol_1 == character_3 or symbol_2 == character_3 or symbol_3 == character_3:
                continue
            counter += 1
            transformed_symbol_1 = chr(symbol_1)
            transformed_symbol_2 = chr(symbol_2)
            transformed_symbol_3 = chr(symbol_3)
            print(f"{transformed_symbol_1}{transformed_symbol_2}{transformed_symbol_3}", end=" ")

print(counter)

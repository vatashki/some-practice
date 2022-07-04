hundreds_upper_range = int(input())
tens_upper_range = int(input())
ones_upper_range = int(input())

for hundreds in range(1, hundreds_upper_range + 1):
    if hundreds % 2 != 0:
        continue
    for tens in range(1, tens_upper_range + 1):
        if tens < 2 or tens > 7:
            continue
        if tens == 4 or tens == 6:
            continue
        for ones in range(1, ones_upper_range + 1):
            if ones % 2 != 0:
                continue
            print(f"{hundreds} {tens} {ones}")

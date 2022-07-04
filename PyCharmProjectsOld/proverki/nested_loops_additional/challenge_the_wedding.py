number_of_men = int(input())
number_of_women = int(input())
number_of_tables = int(input())

occupied_tables = 0

for men in range(1, number_of_men + 1):
    for women in range(1, number_of_women + 1):
        occupied_tables += 1
        print(f"({men} <-> {women})", end=" ")
        if occupied_tables == number_of_tables:
            break
    if occupied_tables == number_of_tables:
        break

year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    if str(year) [0] != str(year) [1] and str(year) [0] != str(year) [2] and str(year) [0] != str(year) [3] and str(year) [1] != str(year) [2] and str(year) [1] != str(year) [3] and str(year) [2] != str(year) [3]:
        is_happy_year = True

print(year)

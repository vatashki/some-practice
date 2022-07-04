n = int(input())

is_odd = False

for numbers in range(0, n):
    number = int(input())
    if number % 2 == 0:
        continue
    if number % 2 != 0:
        print(f"{number} is odd!")
        is_odd = True
        break

if not is_odd:
    print("All numbers are even.")


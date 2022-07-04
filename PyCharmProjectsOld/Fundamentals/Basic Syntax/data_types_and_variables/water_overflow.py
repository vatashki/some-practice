number_of_pours = int(input())

liters_poured = 0

for pours in range(number_of_pours):
    liters_per_pour = int(input())
    if liters_per_pour + liters_poured > 255:
        print("Insufficient capacity!")
        continue
    liters_poured += liters_per_pour

print(liters_poured)


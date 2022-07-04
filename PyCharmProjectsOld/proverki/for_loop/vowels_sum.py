text = input()

total = 0

for char in text:
    if char == "a":
        total += 1
    if char == "e":
        total += 2
    if char == "i":
        total += 3
    if char == "o":
        total += 4
    if char == "u":
        total += 5

print(total)
factor = int(input())
count = int(input())

list_to_fill = []

for n in range(1, count + 1):
    list_to_fill.append(n * factor)

print(list_to_fill)

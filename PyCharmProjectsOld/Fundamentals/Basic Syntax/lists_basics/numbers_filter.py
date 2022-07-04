number_of_lines = int(input())

even = []
odd = []
negative = []
positive = []

for n in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 == 0:
        even += [current_number]
    if current_number % 2 !=0:
        odd += [current_number]
    if current_number < 0:
        negative += [current_number]
    if current_number >= 0:
        positive += [current_number]

command = input()

if command == 'even':
    print(even)
if command == 'odd':
    print(odd)
if command == 'negative':
    print(negative)
if command == 'positive':
    print(positive)

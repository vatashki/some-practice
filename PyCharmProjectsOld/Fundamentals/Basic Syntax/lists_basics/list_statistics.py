number_of_lines = int(input())

positives_list = []
negatives_list = []

for n in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        positives_list.append(current_number)
    if current_number < 0:
        negatives_list.append(current_number)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")

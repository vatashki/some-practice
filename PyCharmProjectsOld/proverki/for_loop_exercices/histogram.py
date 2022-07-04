n_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(n_numbers):
    current_number = int(input())
    if current_number < 200:
        p1 = p1 + 1
    elif 200 <= current_number <= 399:
        p2 = p2 + 1
    elif 399 < current_number <= 599:
        p3 = p3 + 1
    elif 599 < current_number <= 799:
        p4 = p4 + 1
    elif 799 < current_number <= 1000:
        p5 = p5 + 1

p_total = p1 + p2 + p3 + p4 + p5

p1_percent = p1 / p_total * 100
p2_percent = p2 / p_total * 100
p3_percent = p3 / p_total * 100
p4_percent = p4 / p_total * 100
p5_percent = p5 / p_total * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
divisor = int(input())
boundary = int(input())

largest_number = 0

for n in range(1, boundary + 1):
    if n % divisor == 0:
        if n > largest_number:
            largest_number = n


print(largest_number)

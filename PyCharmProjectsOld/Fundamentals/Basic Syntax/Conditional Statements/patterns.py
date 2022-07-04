number = int(input())

for sign in range(1, number + 1):
    print(sign * "*")

for sign in range(number - 1, 0, -1):
    print(sign * "*")

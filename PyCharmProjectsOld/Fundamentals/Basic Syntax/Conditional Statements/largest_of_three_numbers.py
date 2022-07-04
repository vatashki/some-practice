a = int(input())
b = int(input())
c = int(input())

is_the_largest = 0

if a > b and a > c:
    is_the_largest = a
elif b > a and b > c:
    is_the_largest = b
elif c > a and c > b:
    is_the_largest = c

print(is_the_largest)

print(max(a, b, c))
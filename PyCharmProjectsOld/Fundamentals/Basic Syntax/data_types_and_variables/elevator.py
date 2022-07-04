import math
n_persons = int(input())
capacity = int(input())

courses = n_persons / capacity

print(math.ceil(courses))
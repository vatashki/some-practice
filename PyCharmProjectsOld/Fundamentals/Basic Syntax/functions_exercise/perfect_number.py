def perfect_number(a):
    list_of_proper_divisors = []
    for x in range(1, a):
        if a % x == 0:
            list_of_proper_divisors.append(x)
    if sum(list_of_proper_divisors) == a:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number(number)
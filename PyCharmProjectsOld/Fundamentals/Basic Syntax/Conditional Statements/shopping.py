budget = int(input())

command = input()

bought_all_products = False

while command != "End":
    budget -= int(command)
    if budget < 0:
        break
    command = input()
    if command == "End":
        bought_all_products = True

if not bought_all_products:
    print("You went in overdraft!")
if bought_all_products:
    print("You bought everything needed.")


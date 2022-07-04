needed_money = float(input())
money_available = float(input())
spending_counter = 0
total_days = 0
spending_too_many_days = False

while money_available < needed_money:
    action = input()
    current_money = float(input())
    total_days += 1
    if action == "save":
        money_available += current_money
        spending_counter = 0
    else:
        spending_counter += 1
        money_available -= current_money
        if spending_counter == 5:
            spending_too_many_days = True
            break
        if money_available < 0:
            money_available = 0

if spending_too_many_days:
    print("You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
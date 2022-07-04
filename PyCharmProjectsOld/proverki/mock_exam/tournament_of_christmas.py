number_of_days = int(input())

money_won = 0
win_counter_per_day = 0
lose_counter_per_day = 0
days_won = 0
days_lost = 0
total_money = 0

for days in range(number_of_days):
    if win_counter_per_day > lose_counter_per_day:
        money_won = money_won + (money_won * 0.1)
        days_won += 1
    elif win_counter_per_day < lose_counter_per_day:
        days_lost += 1
    total_money += money_won
    money_won = 0
    sport = input()
    outcome = input()
    while sport != "Finish":
        if outcome == "win":
            money_won += 20
            win_counter_per_day += 1
        elif outcome == "lose":
            lose_counter_per_day += 1
        sport = input()
        if sport == "Finish":
            break
        outcome = input()

if win_counter_per_day > lose_counter_per_day:
    money_won = money_won + (money_won * 0.1)
    total_money += money_won
elif win_counter_per_day <= lose_counter_per_day:
    days_lost += 1

if days_won > days_lost:
    total_money = total_money + (total_money * 0.2)
elif days_won <= days_lost:
    money_won = money_won + (money_won * 0.1)
    total_money = total_money + money_won

if days_won > days_lost:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
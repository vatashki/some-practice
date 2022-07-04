tabs = int(input())
salary = float(input())

fee = 0

for site in range(tabs):
    website = input()
    if website == "Facebook":
        fee += 150
    if website == "Instagram":
        fee += 100
    if website == "Reddit":
        fee += 50
    if fee >= salary:
        break

money_left = salary - fee
formatted_money_left = round(money_left)

if fee >= salary:
    print("You have lost your salary.")
else:
    print(formatted_money_left)


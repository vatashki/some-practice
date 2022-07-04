company_name = input()
adult_ticket_number = int(input())
child_ticket_number = int(input())
adult_ticket_price = float(input())
tax = float(input())

total_adult_income = adult_ticket_number * adult_ticket_price + adult_ticket_number * tax
child_ticket_price = adult_ticket_price * 0.3
total_child_income = child_ticket_number * child_ticket_price + child_ticket_number * tax
total_income = total_child_income + total_adult_income

final_income = total_income * 0.2

print(f"The profit of your agency from {company_name} tickets is {final_income:.2f} lv.")


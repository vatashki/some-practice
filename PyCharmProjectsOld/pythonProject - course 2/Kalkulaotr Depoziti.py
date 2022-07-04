deposit_sum = float(input())
deposit_time = int(input())
annual_interest = float(input()) / 100

monthly_interest = deposit_sum * annual_interest / 12
final_sum = deposit_sum + monthly_interest * deposit_time

print(final_sum)
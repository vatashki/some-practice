pages_number = int(input())
pages_per_hour = int(input())
days_number = int(input())

hours_per_book = pages_number / pages_per_hour
hours_per_day = hours_per_book / days_number

print(int(hours_per_day))
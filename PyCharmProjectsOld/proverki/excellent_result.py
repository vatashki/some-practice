grade = float(input())

if grade >= 5.50:
    print("Excellent!")
elif 4.50 <= grade < 5.50:
    print("Very Good!")
elif 3.50 <= grade < 4.50:
    print("Good!")
else:
    print("Poor!")
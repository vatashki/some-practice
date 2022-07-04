age = int(input())

age_range = ""
drink = ""

if age <= 14:
    age_range = "kid"
    drink = "toddy"
    print(f"drink {drink}")
elif 14 < age <= 18:
    age_range = "teen"
    drink = "coke"
    print(f"drink {drink}")
elif 18 < age <= 21:
    age_range = "young adult"
    drink = "beer"
    print(f"drink {drink}")
else:
    age_range = "adult"
    drink = "whisky"
    print(f"drink {drink}")


points = int(input())

if points <= 100:
    bonus_points = 5
    points_and_bonus = points + bonus_points
    if points % 2 == 0:
        final_score = points_and_bonus + 1
        print(bonus_points + 1)
        print(final_score)
    elif points % 10 == 5:
        final_score = points_and_bonus + 2
        print(bonus_points + 2)
        print(final_score)
    else:
        final_score = points_and_bonus + 0
        print(bonus_points + 0)
        print(final_score)
elif 100 < points <= 1000:
    bonus_points = 0.2 * points
    points_and_bonus = points + bonus_points
    if points % 2 == 0:
        final_score = points_and_bonus + 1
        print(bonus_points + 1)
        print(final_score)
    elif points % 10 == 5:
        final_score = points_and_bonus + 2
        print(bonus_points + 2)
        print(final_score)
    else:
        final_score = points_and_bonus + 0
        print(bonus_points + 0)
        print(final_score)
elif points > 1000:
    bonus_points = 0.1 * points
    points_and_bonus = points + bonus_points
    if points % 2 == 0:
        final_score = points_and_bonus + 1
        print(bonus_points + 1)
        print(final_score)
    elif points % 10 == 5:
        final_score = points_and_bonus + 2
        print(bonus_points + 2)
        print(final_score)
    else:
        final_score = points_and_bonus + 0
        print(bonus_points + 0)
        print(final_score)

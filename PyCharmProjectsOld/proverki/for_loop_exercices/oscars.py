actor_name = input()
academy_points = float(input())
judges_number = int(input())

points_to_get = 0
total_points = 0

for judges in range(judges_number):
    judge_name = input()
    judge_points = float(input())
    points_to_get += len(judge_name) * judge_points / 2
    total_points = academy_points + points_to_get
    formatted_total_points = f"{total_points:.1f}"
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {formatted_total_points}!")
        break

points_difference = abs(1250.5 - total_points)
formatted_points_difference = f"{points_difference:.1f}"

if total_points < 1250.5:
    print(f"Sorry, {actor_name} you need {formatted_points_difference} more!")
hours = int(input())
minutes = int(input())

minutes_updated = minutes + 15

if minutes_updated >= 60:
    printed_minutes = minutes_updated - 60
    printed_hours = hours + 1
    if printed_hours >= 24:
        corrected_printed_hours = 24 - printed_hours
        if printed_minutes < 10:
            print(f"{corrected_printed_hours}:0{printed_minutes}")
        else:
            print(f"{corrected_printed_hours}:{printed_minutes}")
    else:
        if printed_minutes < 10:
            print(f"{printed_hours}:0{printed_minutes}")
        else:
            print(f"{printed_hours}:{printed_minutes}")
else:
    printed_minutes = minutes_updated
    printed_hours = hours
    if printed_hours >= 24:
        corrected_printed_hours = 24 - printed_hours
        if printed_minutes < 10:
            print(f"{corrected_printed_hours}:0{printed_minutes}")
        else:
            print(f"{corrected_printed_hours}:{printed_minutes}")
    else:
        if printed_minutes < 10:
            print(f"{printed_hours}:0{printed_minutes}")
        else:
            print(f"{printed_hours}:{printed_minutes}")
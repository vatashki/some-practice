import math

biscuits_per_worker_per_day = int(input())
number_of_workers = int(input())
competing_factory_biscuits = int(input())

total_biscuits_made = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits_made += math.floor((biscuits_per_worker_per_day * number_of_workers) * 0.75)
    else:
        total_biscuits_made += math.floor(biscuits_per_worker_per_day * number_of_workers)

print(f"You have produced {total_biscuits_made} biscuits for the past month.")

percent_difference_if_more = (total_biscuits_made - competing_factory_biscuits) / competing_factory_biscuits * 100
percent_difference_if_less = (competing_factory_biscuits - total_biscuits_made) / competing_factory_biscuits * 100

if total_biscuits_made > competing_factory_biscuits:
    print(f"You produce {percent_difference_if_more:.2f} percent more biscuits.")
else:
    print(f"You produce {percent_difference_if_less:.2f} percent less biscuits.")


pool_volume =int(input())
pipe_1_output = int(input())
pipe_2_output = int(input())
hours_away = float(input())

total_output = pipe_1_output + pipe_2_output
pipe_output_final_volume = total_output * hours_away
pipe_1_total_volume = pipe_1_output * hours_away
pipe_2_total_volume = pipe_2_output * hours_away

both_pipes_fraction = pipe_output_final_volume / pool_volume * 100

overflow_volume = pipe_output_final_volume - pool_volume

pipe_1_fraction = pipe_1_total_volume / pipe_output_final_volume * 100
pipe_2_fraction = pipe_2_total_volume / pipe_output_final_volume * 100

if pipe_output_final_volume <= pool_volume:
    print(f"The pool is {both_pipes_fraction:.2f}% full. Pipe 1: {pipe_1_fraction:.2f}%. Pipe 2: {pipe_2_fraction:.2f}%.")
else:
    print(f"For {hours_away:.2f} hours the pool overflows with {overflow_volume:.2f} liters.")

degrees_celsius = float(input())

degrees_fahrenheit = degrees_celsius * 1.8 + 32

formated_degrees_fahrenheit = "{:.2f}".format(degrees_fahrenheit)

print(formated_degrees_fahrenheit)
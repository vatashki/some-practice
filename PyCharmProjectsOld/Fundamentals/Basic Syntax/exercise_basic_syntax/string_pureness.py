number_of_strings = int(input())

#string_is_pure = True

#for string in range(number_of_strings):
#    current_string = input()
 #   for symbol in current_string:
  #      if symbol == "." or symbol == "," or symbol == "_":
   #         string_is_pure = False
    #if not string_is_pure:
     #   print(f"{current_string} is not pure!")
    #if string_is_pure:
     #   print(f"{current_string} is pure.")

for string in range(number_of_strings):
    current_string = input()
    if '.' in current_string or ',' in current_string or '_' in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

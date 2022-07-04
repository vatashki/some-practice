# for number in range(1, 20 + 1):
# if number % 2 == 0:
#   print(number)
#   continue # = continue loop
# break = stop loop
#   print("Number is odd")

#text = input()

#for letter in range(0, len(text)):
#    print(text[letter])

text = input()
for index, character in enumerate(text):
    print(f"Index -> {index}, character -> {character}")
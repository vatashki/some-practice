searched_book = input()
book_count = 0
book_is_found = False
next_book = input()

while next_book != "No More Books":
    if next_book == searched_book:
        book_is_found = True
        break
    book_count += 1
    next_book = input()

if book_is_found:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")


searched_book = input()
book_count = 0
book_is_found = False
next_book = input()

while next_book != "No more books":
    if next_book == searched_book:
        book_is_found = True
        break
    book_count += 1
    next_book = input()


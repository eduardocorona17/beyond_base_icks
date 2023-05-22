def reading_list(books):
    print('Here are the books I will read: ')
    num_of_books = 0
    for book in books:
        print(book)
        num_of_books += 1
    print(num_of_books, 'books total.')

def count_book_points(books):
    points = 0          # 1 step
    for book in books:  # n * steps in the loop
        points += 1     # 1 step

    for book in books:                  # n * steps in the loop
        if 'by Al Sweigart' in book:    # 1 step
            points += 1                 # 1 step
    return points                       # 1 step



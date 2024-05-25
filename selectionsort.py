def selection_sort_books(books):
    n = len(books)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if books[j][1] < books[min_idx][1]:
                min_idx = j
        books[i], books[min_idx] = books[min_idx], books[i]
    return books
books = [("Book a", 50), ("Book j", 30), ("Book e", 40), ("Book z", 20)]
sorted_books = selection_sort_books(books)
for book in sorted_books:
    print("Book: " + book[0] + " Height: " + str(book[1]))
#O(n^2)
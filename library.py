from books import Books

class Library:

    def __init__(self):
        self.books = []

    def new_book(self, name, author, category, rating, cost=None):
        self.books.append(Books(name, author, category, rating, cost))

    def modify_bookName(self, name, book_id ):
        for book in self.books:
            if book.id == book_id:
                book.name = name

    def modify_bookAuthor(self, author, book_id):
        for book in self.books:
            if book.id == book_id:
                book.author = author

    def modify_bookCategory(self, category, book_id):
        for book in self.books:
            if book.id == book_id:
                book.category = category

    def modify_bookRating(self, rating, book_id):
        for book in self.books:
            if book.id == book_id:
                book.rating = rating

    def find_author(self, author):
        for book in self.books:
            if author == book.author:
                print(author, ':', book.name)

    def search(self,filter):
        already_printed = []
        for book in self.books:
            if book.match(filter) == True:
                already_printed.append(book)
            return already_printed
        return [book for book in self.books if book.match(filter)]


from library import  Library
from books import Books
import sys

class Menu:
    def __init__(self):
        self.library = Library()
        self.choices = {
            "1": self.show_books,
            "2": self.search_books,
            "3": self.add_new_book,
            "4": self.modify_book,
            "5": self.quit
        }

    def display_menu(self):
        print("""
    Library menu:

    1. Show all books you have read
    2. Search for a book
    3. Add a new book
    4. Modify a book info
    5. Quit
              """)

    def run(self):
        '''Display the menu and respond to choices.'''

        while True:
            self.display_menu()
            choice = input("Hello! What would you like to do today? ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_books(self, books = None):
        if not books:
            books = self.library.books
        for book in books:
            print("{0}: {1}T{2}\nCategory: {3}\nRating: {4}".format(book.id, book.name, book.author, book.category, book.rating))

    def search_books(self):
        filter = input("Search: ")
        books = self.library.search(filter)
        self.show_books(books)

    def add_new_book(self):
        choices = int(input(
            "Hello! We are so happy you have finished another book! Please choose one option from the following: \n"
            "1. You have bought a book \n"
            "2. You have already owned the book \n"
            "3. You got the book from a library \n"
                        ))

        if choices == int(1):
            bookName = str(input("Please enter the book's name: "))
            bookAuthor = str(input("Please enter the name of the author: "))
            bookCategory = str(input("Please enter the book's category: "))
            bookRating = int(input("How did you like the book? (1-5) "))
            bookCost = int(input("How much did the book cost (RSD)? "))
            Books.updated_monthly_money(bookCost)
            print("You have left: {0} RSD".format(Books.monthly_money))
            self.library.new_book(bookName,bookAuthor, bookCategory, bookRating, bookCost )

        else:
            bookName = str(input("Please enter the book's name: "))
            bookAuthor = str(input("Please enter the name of the author: "))
            bookCategory = str(input("Please enter the book's category: "))
            bookRating = int(input("How did you like the book? (1-5) "))
            self.library.new_book(bookName, bookAuthor, bookCategory, bookRating)


    def modify_book(self):
        id = int(input("Please input the book's id: "))
        book = self.library.search(id)
        self.show_books(book)
        question = str(input("What would you like to modify? (name, author, category, rating? "))
        if question == "name":
            name = str(input("Please enter the new name for this book: "))
            self.library.modify_bookName(name, id)
            print("You have successfully changed the book's name!")
        if question == "author":
            author = str(input(("Please enter the author's name: ")))
            self.library.modify_bookAuthor(author, id)
            print("You have successfully changed the author's name!")
        if question == "category":
            category = str(input("Please provide another category for this book: "))
            self.library.modify_bookCategory(category, id)
            print("You have successfully changed the book's catagory!")
        if question == "rating":
            rating = int(input("Please enter a new rating for this book (1-5): "))
            self.library.modify_bookRating(rating, id)
            print("You have successfully changed the book's rating")
        else:
            print("Sorry, you cannot modify that!")

    def quit(self):
        print("Keep reading!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

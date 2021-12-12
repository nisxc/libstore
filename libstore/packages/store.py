from book import Book
from logger import Logger


class Store:
    def __init__(self):
        # ! file stream + logging handler
        Logger.__init__(self)
        self.__books_list = []

    def add_book(self):
        # ! add try/exect with validation
        book_title = input('Enter book name: ')
        book_author = input('Enter book author: ')
        book_cost = input('Enter book cost: ')
        book = Book(book_title, book_author, book_cost)
        self.__books_list.append(book.getBookInfo())
        print('Book was added successfully')
        Logger.setWarning(self, 'Hello')
        # logger success or error

    def remove_book(self):
        # ! add try/exect with validation
        book_hint = input(
            'Enter book title or author that you want to delete: ')

        for book in self.__books_list:
            for book_value in book.values():
                if book_hint in book_value:
                    self.__books_list.remove(book)
                    break
        print('Book was deleted successfully')
        # logger success or error

    def find_book(self):
        # ! add try/exect with validation
        book_hint = input(
            'Enter book title or author that you want to find: ')
        for book in self.__books_list:
            for book_value in book.values():
                if book_hint in book_value:
                    return book
        print('Book was find successfully')
        # logger success or error


b = Store()
b.add_book()
print(b.find_book())

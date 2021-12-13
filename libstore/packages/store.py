from packages.book import Book
from packages.logger import Logger
from packages.sqlhelper import SQLHelper
from packages.jsonEncoder import JSONEncoder
from packages.exceptions.storeExceptions import BadFileNameException, StoreException, NotExistException


class Store(Book, Logger, JSONEncoder, SQLHelper):
    def __init__(self, name):
        if not name:
            raise StoreException('Name is empty')
        Logger.__init__(self)
        SQLHelper.__init__(self, name)
        self.__books_list = SQLHelper.select(self)

    def add_book(self):
        try:
            while True:
                book_title = input('Enter book name: ')
                book_author = input('Enter book author: ')
                if not self.find_book(book_title) and not self.find_book(book_author):
                    book_cost = input('Enter book cost: ')
                    book = Book(book_title, book_author, book_cost)
                    print('Book was added successfully')
                    Logger.setDebug(self, 'Book was added successfully')
                    SQLHelper.insert(self, book.getBookInfo()['id'], book_title,
                                     book_author, book_cost)
                    break
                else:
                    print('Sorry but book with this name already exist, try again')
                    Logger.setWarning(
                        self, 'Book with this name already exist')
        except:
            print('Some error')

    def remove_book(self):
        try:
            book_hint = input(
                'Enter book title that you want to delete: ')
            book = self.find_book(book_hint)
            if not book:
                Logger.setError(self, 'Book that you want delete not exist')
                raise NotExistException('Book that you want delete not exist')

            self.__books_list.remove(book)
            SQLHelper.delete(self, book['id'])
            print('Book was deleted successfully')
            Logger.setDebug(self, 'Book was deleted successfully')
        except NotExistException as NEE:
            print(NEE.args[0])
        except StoreException as SE:
            print(SE.args[0])
        except:
            print('Overall madness')

    def find_book(self, hint):
        for book in self.__books_list:
            if hint == book['title']:
                return book

    def save_json(self):
        try:
            fileName = input('Enter file name: ')
            if fileName:
                JSONEncoder.__init__(self, fileName)
            else:
                raise BadFileNameException('Bad file name')
        except BadFileNameException as BFE:
            print(BFE.args[0])
        except:
            print('Overall madness')

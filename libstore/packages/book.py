from uuid import uuid4


class Book:
    def __init__(self, title, author, cost):
        self.__id = uuid4().hex
        self.__title = title
        self.__author = author
        self.__cost = cost

    def getBookInfo(self):
        return {
            'id': self.__id,
            'title': self.__title,
            'author': self.__author,
            'cost': self.__cost
        }

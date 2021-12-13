class StoreException(Exception):
    def __init__(self, message='Some store error, sorry'):
        super().__init__(message)


class NotExistException(StoreException):
    def __init__(self, message):
        super().__init__(message)


class BadFileNameException(StoreException):
    def __init__(self, message):
        super().__init__(message)

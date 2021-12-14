class AppException(Exception):
    def __init__(self, message='Some app error, sorry'):
        super().__init__(message)


class WrongOperationException(AppException):
    def __init__(self, message):
        super().__init__(message)


class BadNameException(AppException):
    def __init__(self, message):
        super().__init__(message)

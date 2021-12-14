import logging

FORMAT = '[%(levelname)s] %(asctime)s - %(message)s'


class Logger:
    def __init__(self) -> None:
        self.__formatter = logging.Formatter(FORMAT)
        self.__logger = logging.getLogger(
            __name__)

        self.__logger.setLevel(logging.DEBUG)

        self.__handler = logging.FileHandler('libstore/logs/app.log', mode='a')

        self.__handler.setLevel(logging.DEBUG)
        self.__handler.setFormatter(self.__formatter)

        self.__logger.addHandler(self.__handler)

    def setWarning(self, message):
        self.__logger.warning(message)
        print('Log was saved')

    def setDebug(self, message):
        self.__logger.debug(message)
        print('Log was saved')

    def setError(self, message):
        self.__logger.error(message)
        print('Log was saved')

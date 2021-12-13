import json

from packages.sqlhelper import SQLHelper


class JSONEncoder(SQLHelper):
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__data_list = SQLHelper.select(self)
        print(self.__data_list)
        with open('libstore/exports/' + self.__fileName + '.json', 'a') as fp:
            json.dump(self.__data_list, fp)

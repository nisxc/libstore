import json
import requests
from os import system

URL = 'http://localhost:3000/exports/'
HEADER = {'Content-Type': 'application/json/'}


class RequestHelper():
    def __init__(self, composition):
        self.__composition = composition

    def get(self):
        requests.get(URL).json()

    def post(self):
        requests.post(URL, headers=HEADER, data=json.dumps(
            self.__composition.add_book().getBookInfo()))
        return self.__composition.save_json()

    def put(self):
        book = self.__composition.update_book()[0]
        requests.put(URL + book['id'], headers=HEADER, data=json.dumps(book))
        return self.__composition.save_json()

    def delete(self):
        requests.delete(URL + self.__composition.remove_book()['id'])
        return self.__composition.save_json()

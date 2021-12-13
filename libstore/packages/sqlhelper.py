import sqlite3

CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {table_name} (
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    cost INT NOT NULL
)'''
INSERT_QUERY = '''INSERT INTO {table_name} (id, title, author, cost) VALUES (?, ?, ?, ?)'''
DELETE_QUERY = '''DELETE FROM {table_name} WHERE id=?'''
SELECT_ALL_QUERY = '''SELECT * FROM {table_name}'''
SELECT_QUERY = '''SELECT * FROM {table_name} WHERE title=?'''


class SQLHelper:
    def __init__(self, name):
        try:
            self.__table_name = name
            self.request_connection()
            self.__cur.execute(CREATE_QUERY.format(
                table_name=self.__table_name))
        except:
            print('Some error with data base initial state')
        finally:
            self.__conn.close()

    def request_connection(self):
        # ? init sqllite connection with cursor
        self.__conn = sqlite3.connect(
            'libstore/db/' + str(self.__table_name) + '.db')
        self.__cur = self.__conn.cursor()

    def insert(self, id, title, author, cost):
        try:
            self.request_connection()
            self.__cur.execute(INSERT_QUERY.format(
                table_name=self.__table_name), (id, title, author, cost))
            self.__conn.commit()
        except:
            print('Some error with data base insert state')
        finally:
            self.__conn.close()

    def delete(self, id):
        print(id)
        try:
            self.request_connection()
            self.__cur.execute(DELETE_QUERY.format(
                table_name=self.__table_name), (id,))
            self.__conn.commit()
        except:
            print('Some error with data base delete state')
        finally:
            self.__conn.close()

    def select(self):
        __result = []
        try:
            self.request_connection()
            for (id, title, author, cost) in self.__cur.execute(SELECT_ALL_QUERY.format(
                    table_name=self.__table_name)):
                __result.append({'id': id, 'title': title,
                                'author': author, 'cost': cost})
            return __result
        except:
            print('Some error with data base insert state')
        finally:
            self.__conn.close()

    def find(self, title):
        try:
            self.request_connection()
            return self.view(list((self.__cur.execute(SELECT_QUERY.format(
                table_name=self.__table_name), (title,)))))

        except:
            print('Some error with data base insert state')
        finally:
            self.__conn.close()

    def view(self, list):
        for book in list:
            for b_attr in book:
                print(b_attr, end=' ')
            print()

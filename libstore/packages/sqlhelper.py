import sqlite3

CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    cost INT NOT NULL
)'''
INSERT_QUERY = '''INSERT INTO {table_name} (title, author, cost) VALUES (?, ?, ?)'''
DELETE_QUERY = '''DELETE FROM {table_name} WHERE id=?'''
SELECT_ALL_QUERY = '''SELECT * FROM {table_name}'''
SELECT_QUERY = '''SELECT * FROM {table_name} WHERE title=?'''


class SQLHelper:
    def __init__(self, name):
        # ! add custom error handlers
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

    def insert(self, title, author, cost):
        try:
            self.request_connection()
            self.__cur.execute(INSERT_QUERY.format(
                table_name=self.__table_name), (title, author, cost))
            self.__conn.commit()
        except:
            print('Some error with data base insert state')
        finally:
            self.__conn.close()

    def delete(self):
        try:
            self.view(self.select())
            # ? check if entered id is numeric
            while True:
                id = input('Enter book id to delete: ')
                if id.isnumeric():
                    break

            self.request_connection()
            self.__cur.execute(DELETE_QUERY.format(
                table_name=self.__table_name), (id))
            self.__conn.commit()
        except:
            print('Some error with data base insert state')
        finally:
            self.__conn.close()

    def select(self):
        try:
            self.request_connection()
            return list(self.__cur.execute(SELECT_ALL_QUERY.format(
                table_name=self.__table_name)))
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

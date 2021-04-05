import pymysql
from pymysql.cursors import DictCursor


class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='university',
            password='12345',
            db='university',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self, name, surname, login, password, status):
        sql = "INSERT INTO people (id, name, surname, login, password, status) VALUES (%s, %s, %s, %s, %s, %s)"
        temp = ['NULL', name, surname, login, password, status]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUsers(self):
        sql = "SELECT * FROM people"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        print(data)


    def getUsers_people(self, login, password):
        sql = f"SELECT * FROM people WHERE login = '{login}' and password = '{password}' "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]



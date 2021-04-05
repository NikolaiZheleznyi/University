from StartPage.Registration.database import DataBase
class Registration:
    def __init__(self, name, surname, login, password, status):

        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.status = status
    def database(self):
        db = DataBase()
        db.addUser( self.name, self.surname, self.login, self.password, self.status)





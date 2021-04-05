from StartPage.Registration.database import DataBase



class Authorization:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def get_database(self):
        try:
            db = DataBase()
            user = db.getUsers_people(self.login, self.password)
            print(user)

            if user != ():

                if user['status'] == 'student':
                    return 'stud'
                elif user['status'] == 'teacher':
                    return 'teach'
            else:
                print('Sorry, user is not found')
        except IndexError:
            return False

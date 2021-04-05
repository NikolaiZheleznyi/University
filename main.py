from StartPage.Registration.Registration import Registration
from StartPage.Authorization.Authorization import Authorization
from StartPage.studMenu.studMenu import Stud
from StartPage.teachMenu.teachMenu import Teach
while True:
    try:
        start_page = int(input('For authorization press 1\nFor registration press 2\nFor exit press 3\nEnter the number: '))
        if start_page == 1:
            def my_authorization():
                authorization = Authorization(input('Enter your login: '), input('Enter your password: '))
                data = authorization.get_database()
                if data == False:
                    my_authorization()
                elif data == 'stud':
                    student = Stud()
                    student.student()
                elif data == 'teach':
                    teacher = Teach()
                    teacher.teacher()
            my_authorization()
            break





        elif start_page == 2:
            def registration():
                register = Registration(input('Enter your name: '), input('Enter your surname: '), input('Enter your login: '), input('Enter your password: '), input('Enter your status: '))
                register.database()

            registration()






        elif start_page == 3:
            break
    except ValueError:
        pass


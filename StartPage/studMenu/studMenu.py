class Stud:
    def student(self):
        stud_menu = int(
            input('For see your progress press 1\n For see your inform press 2\nFor exit press 3\nEnter the number: '))
        if stud_menu == 1:
            self.mark()
        elif stud_menu == 2:
            self.info()
        else:
            pass


    def mark(self):
        print('mark')
    def info(self):
        print('info')


class Teach:
    def teacher(self):
        teach_menu = int(
            input('For change course to student press 1\n For change mark to student press 2\nFor general information about the student press 3\nEnter the number: '))
        if teach_menu == 1:
            self.change_course()
        elif teach_menu == 2:
            self.change_mark()
        elif teach_menu == 3:
            self.general_information()


    def change_course(self):
        print('change_course')
    def change_mark(self):
        print('change_mark')
    def general_information(self):
        print('general_information')
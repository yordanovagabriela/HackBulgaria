from manage_data import DataManager


class ConsoleInterface:
    def __init__(self):
        self.database = DataManager('students_and_courses.db')
        self.commands = {
            "read_command": self.read_command,
            "list_students": self.list_students,
            "list_courses": self.list_courses,
            "list_students_courses": self.list_students_courses,
            "list_greatest_students": self.list_greatest_students
        }

    def read_command(self):
        user_input = input('command>')
        self.commands[user_input]()

    def list_students(self):
        students = self.database.list_students()
        for student in students:
            if student['github_profile'] == '' or student['github_profile'] == None:
                print('{} - no github profile'.format(student['name']))
            else:
                print("{} - {}".format(student['name'], student['github_profile']))

    def list_courses(self):
        courses = self.database.list_courses()
        for course in courses:
            print(course['name'])

    def list_students_courses(self):
        info = self.database.list_students_courses()

        for student in info:
            print('{} - {}'.format(student, ', '.join(info[student])))

    def list_greatest_students(self):
        pass

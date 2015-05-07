import json


import sqlite3


class DataManager:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.all_courses = set()
        self.students_list = []

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                github_profile TEXT
                    )
            """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY,
                name TEXT
                    )
            """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students_to_courses (
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id),
                FOREIGN KEY(course_id) REFERENCES courses(course_id))
            """)

    def get_students_info(self):
        with open('courses-students.json', 'r') as file:
            content = json.load(file)
        courses_for_a_student = []

        for student in content:
            name = student['name']
            github = student['github']
            for course_info in student['courses']:
                courses_for_a_student.append(course_info['name'])
                self.all_courses.add(course_info['name'])
            courses = courses_for_a_student
            self.students_list.append((name, github, courses))
            courses_for_a_student = []

    def courses_table(self):
        for course in self.all_courses:
            self.cursor.execute("""INSERT INTO courses(name)
                VALUES (?)""", (course,))
        self.connection.commit()

    def students_and_relation_table(self):
        for student in self.students_list:
            self.cursor.execute("""INSERT INTO students(name, github_profile)
                VALUES (?, ?)""", (student[0], student[1]))
            self.connection.commit()
            student_id = self.cursor.lastrowid

            for course in student[2]:
                self.cursor.execute('SELECT course_id FROM courses WHERE name = ?', (course,))
                course_id = self.cursor.fetchone()
                self.cursor.execute("""INSERT INTO students_to_courses(student_id, course_id)
                VALUES (?, ?)""", (student_id, course_id[0]))
                self.connection.commit()

    def list_students(self):
        return self.cursor.execute('SELECT name, github_profile FROM students')

    def list_courses(self):
        return self.cursor.execute('SELECT name FROM courses')

    def list_students_courses(self):
        content = self.cursor.execute(""" SELECT students.name as s_name, courses.name as c_name FROM
            students, courses JOIN students_to_courses ON
            students_to_courses.student_id = students.student_id
            and students_to_courses.course_id = courses.course_id
            """)

        student_name = 's_name'
        course_name = 'c_name'
        info = {}

        for item in content:
            if item[student_name] not in info:
                info[item[student_name]] = [item[course_name]]
            else:
                info[item[student_name]] += [item[course_name]]

        return info

    def list_greatest_students(self):
        pass

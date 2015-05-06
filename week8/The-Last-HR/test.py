import json


import sqlite3


with open('courses-students.json', 'r') as file:
    content = json.load(file)
students_list = []
all_courses = set()
courses = []


for student in content:
    name = student['name']
    github = student['github']
    for course_info in student['courses']:
        courses.append(course_info['name'])
        all_courses.add(course_info['name'])
    student_course = courses
    students_list.append((name, github, student_course))
    courses = []


connection = sqlite3.connect('dbtest.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                github_profile TEXT
                    )
            """)
cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY,
                name TEXT
                    )
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS students_to_courses (
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id),
                FOREIGN KEY(course_id) REFERENCES courses(course_id))
            """)

for course in all_courses:
    cursor.execute("""INSERT INTO courses(name)
                VALUES (?)""", (course,))
    connection.commit()


for student in students_list:
    cursor.execute("""INSERT INTO students(name, github_profile)
                VALUES (?, ?)""", (student[0], student[1]))
    connection.commit()
    student_id = cursor.lastrowid

    for course in student[2]:
        cursor.execute('SELECT course_id FROM courses WHERE name = ?', (course,))
        course_id = cursor.fetchone()
        cursor.execute("""INSERT INTO students_to_courses(student_id, course_id)
                VALUES (?, ?)""", (student_id, course_id[0]))
        connection.commit()

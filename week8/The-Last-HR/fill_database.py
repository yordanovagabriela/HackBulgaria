from manage_data import DataManager


def main():
    db = DataManager('students_and_courses.db')
    db.create_tables()
    db.get_students_info()
    db.courses_table()
    db.students_and_relation_table()

if __name__ == '__main__':
    main()

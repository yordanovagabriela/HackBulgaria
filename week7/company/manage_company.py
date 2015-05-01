import sqlite3


class CompanyManager:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                monthly_salary INTEGER,
                yearly_bonus INTEGER,
                position TEXT)
            """)

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute("""INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES (?, ?, ?, ?)""", (name, monthly_salary, yearly_bonus, position))
        self.conn.commit()

    def list_employees(self):
        self.cursor.execute('SELECT id, name, position FROM employees')

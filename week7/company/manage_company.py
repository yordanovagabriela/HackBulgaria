import sqlite3


import sys


class CompanyManager:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row
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
        self.cursor.execute("""INSERT INTO employees(name,monthly_salary, yearly_bonus, position)
            VALUES (?, ?, ?, ?)""", (name, monthly_salary, yearly_bonus, position))
        self.conn.commit()

    def list_employees(self):
        return self.cursor.execute('SELECT id, name, position FROM employees')

    def monthly_spending(self):
        monthly_spending = self.cursor.execute('SELECT monthly_salary FROM employees')
        monthly_amount = 0
        for money in monthly_spending:
            monthly_amount = monthly_amount + money['monthly_salary']
        return monthly_amount

    def yearly_spending(self):
        yearly_spending = self.cursor.execute('SELECT yearly_bonus FROM employees')
        MONTHS = 12
        bonus = 0
        for money in yearly_spending:
            bonus = bonus + money['yearly_bonus']
        salaries_spending = self.monthly_spending()*MONTHS
        return salaries_spending + bonus

    def delete_employee(self, id_number):
        self.cursor.execute('DELETE FROM employees WHERE id = ?', (id_number))
        self.conn.commit()

    def update_employee(self, id_number, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute("""UPDATE employees SET name = ?,
                                          monthly_salary = ?,
                                          yearly_bonus = ?,
                                          position = ?
                            WHERE id = ? """, (name, monthly_salary, yearly_bonus, position, id_number))
        self.conn.commit()

    def exit(self):
        sys.exit(0)

from manage_company import CompanyManager

import sqlite3


class console:
    def __init__(self):
        self.manager = CompanyManager('database.db')
        self.commands = {
            "read_command": self.read_command,
            "list_employees": self.list_employees,
            "add_employee": self.add_employee,
            "monthly_spending": self.monthly_spending,
            "yearly_spending": self.yearly_spending,
            "delete_employee": self.delete_employee,
            "update_employee": self.update_employee,
            "exit": self.exit
        }

    def read_command(self):
        user_input = input('command>')
        self.commands[user_input]()

    def list_employees(self):
        employees = self.manager.list_employees()
        for employee in employees:
            print("{} - {} - {}".format(employee['id'], employee['name'], employee['position']))

    def add_employee(self):
        n = input('input name:')
        ms = input('input monthly_salaray:')
        yb = input('input yearly_bonus:')
        p = input('position:')
        self.manager.add_employee(n, ms, yb, p)

    def monthly_spending(self):
        spendings = self.manager.monthly_spending()
        print("The company is spending ${} every month!".format(spendings))

    def yearly_spending(self):
        spendings = self.manager.yearly_spending()
        print("The company is spending ${} every year!".format(spendings))

    def delete_employee(self):
        id_number = input('id>')
        self.manager.delete_employee(id_number)
        print("employee deleted!")

    def update_employee(self):
        id_number = input('id>')
        n = input('name>')
        ms = input('monthly_salaray>')
        yb = input('yearly_bonus>')
        p = input('position>')
        self.manager.update_employee(id_number, n, ms, yb, p)

    def exit(self):
        print("You are now out of the application!")
        self.manager.exit()

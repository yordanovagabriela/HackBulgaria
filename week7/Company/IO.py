from manage_company import CompanyManager


class IO:
    def __init__(self):
        self.manager = CompanyManager('database.db')
        self.commands = {
            "read_command": self.read_command,
            "test": self.test
        }

    def read_command(self):
        user_input = input('command>')
        self.commands[user_input]()

    def list_employees(self):
        employees = self.manager.list_employees()
        for employee in employees:
            print("{} - {} - {}".format(employee.id, employee.name, employee.position))

//da preimenuvam faila !

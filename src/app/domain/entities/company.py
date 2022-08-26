class Company:
    def __init__(self, id, name, employees=None):
        if employees is None:
            employees = set()
        self.id = id
        self.name = name
        self.employees = employees

    def add_employee(self, employee_id):
        self.employees.add(employee_id)

    def has_employee(self, employee_id):
        return employee_id in self.employees

    def remove_employee(self, employee_id):
        self.employees.remove(employee_id)

    def change_name(self, name):
        self.name = name

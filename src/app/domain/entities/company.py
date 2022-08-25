class Company:
    def __init__(self, id, name, employees=None):
        if employees is None:
            employees = []
        self.id = id
        self.name = name
        self.employees = employees

    def add_employee(self, employee_id):
        self.employees.append(employee_id)

    def has_employee(self, employee_id):
        try:
            self.employees.index(employee_id)
            return True
        except ValueError:
            return False

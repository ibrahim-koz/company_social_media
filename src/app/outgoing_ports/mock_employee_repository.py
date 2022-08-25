from src.app.domain.exceptions.employee_not_found_exception import EmployeeNotFoundException
from src.app.domain.repositories.employee_repository import EmployeeRepository


class MockEmployeeRepository(EmployeeRepository):
    def __init__(self):
        self.employees = {}

    def add(self, employee):
        self.employees[employee.id] = employee

    def get_employee_by_id(self, id):
        try:
            return self.employees[id]
        except KeyError:
            raise EmployeeNotFoundException()

    def filter(self, function):
        return list(filter(function, self.employees.values()))

    def update(self, employee):
        self.employees[employee.id] = employee

    def remove_all(self, id):
        try:
            del self.employees[id]
        except KeyError:
            raise EmployeeNotFoundException()

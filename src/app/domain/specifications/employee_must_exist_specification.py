from src.app.domain.exceptions.employee_not_found_exception import EmployeeNotFoundException


class EmployeeMustExistSpecification:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def is_satisfied_by(self, employee_id):
        try:
            self.employee_repository.get_employee_by_id(employee_id)
            return True
        except EmployeeNotFoundException:
            return False

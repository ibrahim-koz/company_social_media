class EmployeeMustExistSpecification:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def is_satisfied(self, employee_id):
        return self.employee_repository.contains(employee_id)

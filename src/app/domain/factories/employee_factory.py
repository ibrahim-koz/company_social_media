from src.app.domain.entities.employee import Employee


class EmployeeFactory:
    def __init__(self, id_generator):
        self.id_generator = id_generator

    def create(self, name, salary, company_id):
        return Employee(self.id_generator.generate(), name, salary, company_id)


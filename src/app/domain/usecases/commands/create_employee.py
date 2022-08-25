from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException


class CreateEmployee:
    def __init__(self, employee_repo, employee_factory, company_must_exist_specification, company_repo):
        self.employee_repo = employee_repo
        self.employee_factory = employee_factory
        self.company_must_exist_specification = company_must_exist_specification
        self.company_repo = company_repo

    def handle(self, create_employee_request):
        name = create_employee_request.name
        salary = create_employee_request.salary
        company_id = create_employee_request.company_id

        if not self.company_must_exist_specification.is_satisfied_by(company_id):
            raise CompanyNotFoundException()

        new_employee = self.employee_factory.create(name, salary, company_id)
        self.employee_repo.add(new_employee)

        company = self.company_repo.get_company_by_id(company_id)
        company.add_employee(new_employee.id)
        self.company_repo.update(company)
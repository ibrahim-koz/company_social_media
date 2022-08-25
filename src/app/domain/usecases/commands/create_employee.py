class CreateEmployee:
    def __init__(self, employee_repository, employee_factory, company_repo):
        self.employee_repository = employee_repository
        self.employee_factory = employee_factory
        self.company_repo = company_repo

    def handle(self, create_employee_request):
        name = create_employee_request.name
        salary = create_employee_request.salary
        company_id = create_employee_request.company_id

        new_employee = self.employee_factory.create(name, salary, company_id)
        self.employee_repository.add(new_employee)

        company = self.company_repo.get_company_by_id(company_id)
        company.add_employee(new_employee.id)
        self.company_repo.update(company)

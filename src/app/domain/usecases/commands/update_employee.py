class UpdateEmployee:
    def __init__(self, employee_repository, company_repository):
        self.employee_repository = employee_repository
        self.company_repository = company_repository

    def handle(self, update_employee_request):
        id = update_employee_request.id
        name = update_employee_request.name
        salary = update_employee_request.salary
        company_id = update_employee_request.company_id
        employee = self.employee_repository.get_employee_by_id(id)
        if name is not None:
            employee.change_name(name)
        if salary is not None:
            employee.change_salary(salary)
        if company_id is not None:
            old_company = self.company_repository.get_company_by_id(employee.company_id)
            new_company = self.company_repository.get_company_by_id(company_id)
            old_company.remove_employee(id)
            new_company.add_employee(id)
            employee.change_company_id(company_id)
            self.company_repository.update(old_company)
            self.company_repository.update(new_company)
        self.employee_repository.update(employee)

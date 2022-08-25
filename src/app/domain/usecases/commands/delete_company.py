from src.app.domain.requests.delete_employee_request import DeleteEmployeeRequest


class DeleteCompany:
    def __init__(self, company_repository, delete_employee):
        self.company_repository = company_repository
        self.delete_employee = delete_employee

    def handle(self, delete_company_request):
        id = delete_company_request.id
        company = self.company_repository.get_company_by_id(id)
        employee_ids = company.employees

        delete_employee_requests = [DeleteEmployeeRequest(id) for id in employee_ids]
        for request in delete_employee_requests:
            self.delete_employee.handle(request)
        self.company_repository.remove(id)

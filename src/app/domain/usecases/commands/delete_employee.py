from src.app.domain.requests.delete_entry_request import DeleteEntryRequest


class DeleteEmployee:
    def __init__(self, company_repository, employee_repository, delete_entry):
        self.employee_repository = employee_repository
        self.delete_entry = delete_entry
        self.company_repository = company_repository

    def handle(self, delete_employee_request):
        id = delete_employee_request.id
        employee = self.employee_repository.get_employee_by_id(id)
        company = self.company_repository.get_company_by_id(employee.company_id)
        entry_ids = employee.entries

        delete_entry_requests = [DeleteEntryRequest(id) for id in entry_ids]
        for delete_entry_request in delete_entry_requests:
            self.delete_entry.handle(delete_entry_request)
        self.employee_repository.remove(id)
        company.remove_employee(id)
        self.company_repository.update(company)
from functools import reduce


class GetFeed:
    def __init__(self, company_repository, employee_repository, entry_repository):
        self.company_repository = company_repository
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, get_feed_request):
        company_id = get_feed_request.company_id
        company = self.company_repository.get_company_by_id(company_id)
        employees = (self.employee_repository.get_employee_by_id(employee_id) for employee_id in company.employees)
        entries = sorted([self.entry_repository.get_entry_by_id(entry_id) for entry_id in
                          reduce(lambda x, y: x | y, (employee.entries for employee in employees))])
        return entries

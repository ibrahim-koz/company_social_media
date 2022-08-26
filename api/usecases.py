from src.app.domain.requests.delete_employee_request import DeleteEmployeeRequest
from src.app.domain.requests.delete_entry_request import DeleteEntryRequest
from functools import reduce


class CreateCompany:
    def __init__(self, company_repository, company_factory):
        self.company_repository = company_repository
        self.company_factory = company_factory

    def handle(self, create_company_request):
        name = create_company_request.name
        new_company = self.company_factory.create(name)
        self.company_repository.add(new_company)


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


class CreateEntry:
    def __init__(self, entry_repository, entry_factory, employee_repository):
        self.entry_factory = entry_factory
        self.entry_repository = entry_repository
        self.employee_repository = employee_repository

    def handle(self, create_entry_request):
        title = create_entry_request.title
        content = create_entry_request.content
        employee_id = create_entry_request.employee_id

        new_entry = self.entry_factory.create(title, content, employee_id)
        self.entry_repository.add(new_entry)

        employee = self.employee_repository.get_employee_by_id(employee_id)
        employee.add_entry(new_entry.id)
        self.employee_repository.update(employee)


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


class DeleteEntry:
    def __init__(self, employee_repository, entry_repository):
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, delete_entry_request):
        id = delete_entry_request.id
        entry = self.entry_repository.get_entry_by_id(id)
        employee = self.employee_repository.get_employee_by_id(entry.employee_id)
        self.entry_repository.remove(id)
        employee.remove_entry(id)
        self.employee_repository.update(employee)


class UpdateCompany:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def handle(self, update_company_request):
        id = update_company_request.id
        name = update_company_request.name
        company = self.company_repository.get_company_by_id(id)
        if name is not None:
            company.change_name(name)
        self.company_repository.update(company)


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


class UpdateEntry:
    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def handle(self, update_entry_request):
        id = update_entry_request.id
        title = update_entry_request.title
        content = update_entry_request.content
        entry = self.entry_repository.get_entry_by_id(id)
        if title is not None:
            entry.change_title(title)
        if content is not None:
            entry.change_content(content)
        self.entry_repository.update(entry)


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


class GetTimeline:
    def __init__(self, employee_repository, entry_repository):
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, get_timeline_request):
        employee_id = get_timeline_request.employee_id
        employee = self.employee_repository.get_employee_by_id(employee_id)
        entries = sorted([self.entry_repository.get_entry_by_id(entry_id) for entry_id in employee.entries])
        return entries


class ReadCompany:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def handle(self, read_company_request):
        id = read_company_request.id
        return self.company_repository.get_company_by_id(id)


class ReadEmployee:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def handle(self, read_employee_request):
        id = read_employee_request.id
        return self.employee_repository.get_employee_by_id(id)


class ReadEntry:
    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def handle(self, read_entry_request):
        id = read_entry_request.id
        return self.entry_repository.get_entry_by_id(id)

from functools import reduce


class CreateCompany:
    def __init__(self, company_repository, company_factory):
        self.company_repository = company_repository
        self.company_factory = company_factory

    def handle(self, create_company_request):
        name = create_company_request['name']
        new_company = self.company_factory.create(name)
        self.company_repository.save(new_company)
        return new_company


class CreateEmployee:
    def __init__(self, employee_repository, employee_factory, company_repo):
        self.employee_repository = employee_repository
        self.employee_factory = employee_factory
        self.company_repo = company_repo

    def handle(self, create_employee_request):
        name = create_employee_request['name']
        salary = create_employee_request['salary']
        company_id = create_employee_request['company_id']

        company = self.company_repo.get_company_by_id(company_id)
        new_employee = self.employee_factory.create(name, salary, company)

        self.employee_repository.save(new_employee)
        return new_employee


class CreateEntry:
    def __init__(self, entry_repository, entry_factory, employee_repository):
        self.entry_factory = entry_factory
        self.entry_repository = entry_repository
        self.employee_repository = employee_repository

    def handle(self, create_entry_request):
        title = create_entry_request['title']
        content = create_entry_request['content']
        employee_id = create_entry_request['employee_id']

        employee = self.employee_repository.get_employee_by_id(employee_id)
        new_entry = self.entry_factory.create(title, content, employee)

        self.entry_repository.save(new_entry)

        employee.add_entry(new_entry.id)
        self.employee_repository.save(employee)
        return new_entry


class DeleteCompany:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def handle(self, delete_company_request):
        id = delete_company_request.id
        self.company_repository.remove(id)


class DeleteEmployee:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def handle(self, delete_employee_request):
        id = delete_employee_request.id
        self.employee_repository.remove(id)


class DeleteEntry:
    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def handle(self, delete_entry_request):
        id = delete_entry_request.id
        self.entry_repository.remove(id)


class UpdateCompany:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def handle(self, update_company_request):
        id = update_company_request['id']
        name = update_company_request.get('name', None)
        company = self.company_repository.get_company_by_id(id)
        if name is not None:
            company.change_name(name)
        self.company_repository.save(company)
        return company


class UpdateEmployee:
    def __init__(self, employee_repository, company_repository):
        self.employee_repository = employee_repository
        self.company_repository = company_repository

    def handle(self, update_employee_request):
        id = update_employee_request['id']
        name = update_employee_request.get('name', None)
        salary = update_employee_request.get('salary', None)
        company_id = update_employee_request.get('company_id', None)
        employee = self.employee_repository.get_employee_by_id(id)
        if name is not None:
            employee.change_name(name)
        if salary is not None:
            employee.change_salary(salary)
        if company_id is not None:
            self.change_company(company_id, employee)
        self.employee_repository.save(employee)
        return employee

    def change_company(self, company_id, employee):
        old_company = self.company_repository.get_company_by_id(employee.company_id)
        new_company = self.company_repository.get_company_by_id(company_id)
        employee.change_company(new_company.id)
        self.company_repository.save(old_company)
        self.company_repository.save(new_company)


class UpdateEntry:
    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def handle(self, update_entry_request):
        id = update_entry_request['id']
        title = update_entry_request.get('title', None)
        content = update_entry_request.get('content', None)
        entry = self.entry_repository.get_entry_by_id(id)
        if title is not None:
            entry.change_title(title)
        if content is not None:
            entry.change_content(content)
        self.entry_repository.save(entry)
        return entry


class GetFeed:
    def __init__(self, company_repository, employee_repository, entry_repository):
        self.company_repository = company_repository
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, get_feed_request):
        company_id = get_feed_request.company_id
        company = self.company_repository.get_company_by_id(company_id)
        employees = company.employees
        employees_ = [employee.entries for employee in employees]
        if len(employees_) == 0:
            return []
        entries = [reduce(lambda x, y: x | y, employees_)][0].order_by('-date')
        return list(entries)


class GetTimeline:
    def __init__(self, employee_repository, entry_repository):
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, get_timeline_request):
        employee_id = get_timeline_request.employee_id
        employee = self.employee_repository.get_employee_by_id(employee_id)
        entries = employee.entries.order_by('-date')
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

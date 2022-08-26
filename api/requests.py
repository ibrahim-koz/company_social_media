class CreateCompanyRequest:
    def __init__(self, name):
        self.name = name


class CreateEmployeeRequest:
    def __init__(self, name, salary, company_id):
        self.name = name
        self.salary = salary
        self.company_id = company_id


class CreateEntryRequest:
    def __init__(self, title, content, employee_id):
        self.title = title
        self.content = content
        self.employee_id = employee_id


class DeleteCompanyRequest:
    def __init__(self, id):
        self.id = id


class DeleteEmployeeRequest:
    def __init__(self, id):
        self.id = id


class DeleteEntryRequest:
    def __init__(self, id):
        self.id = id


class GetFeedRequest:
    def __init__(self, company_id):
        self.company_id = company_id


class GetTimelineRequest:
    def __init__(self, employee_id):
        self.employee_id = employee_id


class ReadCompanyRequest:
    def __init__(self, id):
        self.id = id


class ReadEmployeeRequest:
    def __init__(self, id):
        self.id = id


class ReadEntryRequest:
    def __init__(self, id):
        self.id = id


class UpdateCompanyRequest:
    def __init__(self, id, name=None):
        self.id = id
        self.name = name


class UpdateEmployeeRequest:
    def __init__(self, id, name=None, salary=None, company_id=None):
        self.id = id
        self.name = name
        self.salary = salary
        self.company_id = company_id


class UpdateEntryRequest:
    def __init__(self, id, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content

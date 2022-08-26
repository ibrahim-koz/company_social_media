class UpdateEmployeeRequest:
    def __init__(self, id, name=None, salary=None, company_id=None):
        self.id = id
        self.name = name
        self.salary = salary
        self.company_id = company_id

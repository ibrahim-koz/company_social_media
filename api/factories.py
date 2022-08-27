from api.models import Company, Employee, Entry


class CompanyFactory:
    def create(self, name):
        return Company(name=name)


class EmployeeFactory:
    def create(self, name, salary, company):
        return Employee(name=name, salary=salary, company=company)


class EntryFactory:
    def create(self, title, content, employee):
        return Entry(title=title, content=content, employee=employee)

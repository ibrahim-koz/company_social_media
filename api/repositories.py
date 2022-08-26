from models import Company, Employee, Entry


class CompanyRepository:
    def add(self, company):
        company.save()

    def get_company_by_id(self, id):
        return Company.objects.get(id=id)

    def filter(self, function):
        return Company.objects.filter(function)

    def update(self, company):
        return company.save()

    def remove(self, id):
        return Company.objects.get(id=id).delete()


class EmployeeRepository:
    def add(self, employee):
        employee.save()

    def get_employee_by_id(self, id):
        return Employee.objects.get(id=id)

    def filter(self, function):
        return Employee.objects.filter(function)

    def update(self, employee):
        employee.save()

    def remove(self, id):
        return Employee.objects.get(id=id).delete()


class EntryRepository:
    def add(self, entry):
        entry.save()

    def get_entry_by_id(self, id):
        return Entry.objects.get(id=id)

    def filter(self, function):
        return Entry.objects.filter(function)

    def update(self, entry):
        entry.save()

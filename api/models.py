from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def add_employee(self, employee_id):
        Employee.objects.get(id=employee_id).company = self

    def has_employee(self, employee_id):
        return Employee.objects.filter(company=self).filter(id=employee_id).exists()

    def remove_employee(self, employee_id):
        Employee.objects.filter(company=self).get(id=employee_id).delete()

    def change_name(self, name):
        self.name = name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def add_entry(self, entry_id):
        Entry.objects.get(id=entry_id).employee = self

    def has_entry(self, entry_id):
        return Entry.objects.filter(employee=self).filter(id=entry_id).exists()

    def remove_entry(self, entry_id):
        Entry.objects.filter(employee=self).get(id=entry_id).delete()

    def change_name(self, name):
        self.name = name

    def change_salary(self, salary):
        self.salary = salary

    def change_company(self, company_id):
        self.company = Company.objects.get(id=company_id)


class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def change_title(self, title):
        self.title = title

    def change_content(self, content):
        self.content = content

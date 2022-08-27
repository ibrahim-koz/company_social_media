from api.factories import *
from api.repositories import *
from api.usecases import *

company_repository = CompanyRepository()
employee_repository = EmployeeRepository()
entry_repository = EntryRepository()

company_factory = CompanyFactory()
employee_factory = EmployeeFactory()
entry_factory = EntryFactory()

create_company = CreateCompany(company_repository, company_factory)
delete_company = DeleteCompany(company_repository)
read_company = ReadCompany(company_repository)
update_company = UpdateCompany(company_repository)

create_employee = CreateEmployee(employee_repository, employee_factory, company_repository)
delete_employee = DeleteEmployee(employee_repository)
read_employee = ReadEmployee(employee_repository)
update_employee = UpdateEmployee(employee_repository, company_repository)

create_entry = CreateEntry(entry_repository, entry_factory, employee_repository)
delete_entry = DeleteEntry(entry_repository)
read_entry = ReadEntry(entry_repository)
update_entry = UpdateEntry(entry_repository)

read_feed = GetFeed(entry_repository, employee_repository, company_repository)
read_timeline = GetTimeline(entry_repository, employee_repository)

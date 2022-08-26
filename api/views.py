# Create your views here.
from api.factories import *
from api.repositories import *
from api.requests import *
from api.usecases import *


def company(request):
    if request.method == 'POST':
        create_company_request = CreateCompanyRequest(request.POST)
        create_company = CreateCompany(CompanyRepository(), CompanyFactory())
        return create_company.handle(create_company_request)

    elif request.method == 'DELETE':
        delete_company_request = DeleteCompanyRequest(request.POST)
        delete_company = DeleteCompany(CompanyRepository())
        return delete_company.handle(delete_company_request)

    elif request.method == 'GET':
        read_company_request = ReadCompanyRequest(request.GET)
        read_company = ReadCompany(CompanyRepository())
        return read_company.handle(read_company_request)

    elif request.method == 'PUT':
        update_company_request = UpdateCompanyRequest(request.POST)
        update_company = UpdateCompany(CompanyRepository())
        return update_company.handle(update_company_request)


def employee(request):
    if request.method == 'POST':
        create_employee_request = CreateEmployeeRequest(request.POST)
        create_employee = CreateEmployee(EmployeeRepository(), EmployeeFactory(), CompanyRepository())
        return create_employee.handle(create_employee_request)

    elif request.method == 'DELETE':
        delete_employee_request = DeleteEmployeeRequest(request.POST)
        delete_employee = DeleteEmployee(EmployeeRepository())
        return delete_employee.handle(delete_employee_request)

    elif request.method == 'GET':
        read_employee_request = ReadEmployeeRequest(request.GET)
        read_employee = ReadEmployee(EmployeeRepository())
        return read_employee.handle(read_employee_request)

    elif request.method == 'PUT':
        update_employee_request = UpdateEmployeeRequest(request.POST)
        update_employee = UpdateEmployee(EmployeeRepository())
        return update_employee.handle(update_employee_request)


def entry(request):
    if request.method == 'POST':
        create_entry_request = CreateEntryRequest(request.POST)
        create_entry = CreateEntry(EntryRepository(), EntryFactory(), EmployeeRepository())
        return create_entry.handle(create_entry_request)

    elif request.method == 'DELETE':
        delete_entry_request = DeleteEntryRequest(request.POST)
        delete_entry = DeleteEntry(EntryRepository())
        return delete_entry.handle(delete_entry_request)

    elif request.method == 'GET':
        read_entry_request = ReadEntryRequest(request.GET)
        read_entry = ReadEntry(EntryRepository())
        return read_entry.handle(read_entry_request)

    elif request.method == 'PUT':
        update_entry_request = UpdateEntryRequest(request.POST)
        update_entry = UpdateEntry(EntryRepository())
        return update_entry.handle(update_entry_request)


def feed(request):
    if request.method == 'GET':
        read_feed_request = GetFeedRequest(request.GET)
        read_feed = GetFeed(EntryRepository(), EmployeeRepository(), CompanyRepository())
        return read_feed.handle(read_feed_request)


def timeline(request):
    if request.method == 'GET':
        read_timeline_request = GetTimelineRequest(request.GET)
        read_timeline = GetTimeline(EntryRepository(), EmployeeRepository(), CompanyRepository())
        return read_timeline.handle(read_timeline_request)

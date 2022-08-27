# Create your views here.
from composition_root import *
from api.requests import *


def company(request):
    if request.method == 'POST':
        create_company_request = CreateCompanyRequest(request.POST)
        return create_company.handle(create_company_request)

    elif request.method == 'DELETE':
        delete_company_request = DeleteCompanyRequest(request.POST)
        return delete_company.handle(delete_company_request)

    elif request.method == 'GET':
        read_company_request = ReadCompanyRequest(request.GET)
        return read_company.handle(read_company_request)

    elif request.method == 'PUT':
        update_company_request = UpdateCompanyRequest(request.POST)
        return update_company.handle(update_company_request)


def employee(request):
    if request.method == 'POST':
        create_employee_request = CreateEmployeeRequest(request.POST)
        return create_employee.handle(create_employee_request)

    elif request.method == 'DELETE':
        delete_employee_request = DeleteEmployeeRequest(request.POST)
        return delete_employee.handle(delete_employee_request)

    elif request.method == 'GET':
        read_employee_request = ReadEmployeeRequest(request.GET)
        return read_employee.handle(read_employee_request)

    elif request.method == 'PUT':
        update_employee_request = UpdateEmployeeRequest(request.POST)
        return update_employee.handle(update_employee_request)


def entry(request):
    if request.method == 'POST':
        create_entry_request = CreateEntryRequest(request.POST)
        return create_entry.handle(create_entry_request)

    elif request.method == 'DELETE':
        delete_entry_request = DeleteEntryRequest(request.POST)
        return delete_entry.handle(delete_entry_request)

    elif request.method == 'GET':
        read_entry_request = ReadEntryRequest(request.GET)
        return read_entry.handle(read_entry_request)

    elif request.method == 'PUT':
        update_entry_request = UpdateEntryRequest(request.POST)
        return update_entry.handle(update_entry_request)


def feed(request):
    if request.method == 'GET':
        read_feed_request = GetFeedRequest(request.GET)
        return read_feed.handle(read_feed_request)


def timeline(request):
    if request.method == 'GET':
        read_timeline_request = GetTimelineRequest(request.GET)
        return read_timeline.handle(read_timeline_request)

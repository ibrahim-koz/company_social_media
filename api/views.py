from .composition_root import *
from .requests import *

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class CompanyView(APIView):
    def post(self, request, *args, **kwargs):
        create_company_request = CreateCompanyRequest(request.data['name'])
        company = create_company.handle(create_company_request)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def delete(self, request, id, *args, **kwargs):
        delete_company_request = DeleteCompanyRequest(id)
        delete_company.handle(delete_company_request)
        return Response(status=204)

    def get(self, request, id, *args, **kwargs):
        read_company_request = ReadCompanyRequest(id)
        company = read_company.handle(read_company_request)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        update_company_request = UpdateCompanyRequest(request.data['id'], request.data.get('name', None))
        company = update_company.handle(update_company_request)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


class EmployeeView(APIView):
    def post(self, request, *args, **kwargs):
        create_employee_request = CreateEmployeeRequest(request.data['name'], request.data['salary'],
                                                        request.data['company_id'])
        employee = create_employee.handle(create_employee_request)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def delete(self, request, id, *args, **kwargs):
        delete_employee_request = DeleteEmployeeRequest(id)
        delete_employee.handle(delete_employee_request)
        return Response(status=204)

    def get(self, request, id, *args, **kwargs):
        read_employee_request = ReadEmployeeRequest(id)
        employee = read_employee.handle(read_employee_request)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        update_employee_request = UpdateEmployeeRequest(request.data['id'], request.data.get('name', None),
                                                        request.data.get('salary', None),
                                                        request.data.get('company_id', None))
        employee = update_employee.handle(update_employee_request)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class EntryView(APIView):
    def post(self, request, *args, **kwargs):
        create_entry_request = CreateEntryRequest(request.data['title'], request.data['content'],
                                                  request.data['employee_id'])
        entry = create_entry.handle(create_entry_request)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)

    def delete(self, request, id, *args, **kwargs):
        delete_entry_request = DeleteEntryRequest(id)
        delete_entry.handle(delete_entry_request)
        return Response(status=204)

    def get(self, request, id, *args, **kwargs):
        read_entry_request = ReadEntryRequest(id)
        entry = read_entry.handle(read_entry_request)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        update_entry_request = UpdateEntryRequest(request.data['id'], request.data.get('title', None),
                                                  request.data.get('content', None))
        entry = update_entry.handle(update_entry_request)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)


class FeedView(APIView):
    def get(self, request, *args, **kwargs):
        read_feed_request = GetFeedRequest(request.GET)
        return read_feed.handle(read_feed_request)


class TimelineView(APIView):
    def get(self, request, *args, **kwargs):
        read_timeline_request = GetTimelineRequest(request.GET)
        return read_timeline.handle(read_timeline_request)

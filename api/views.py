from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from .composition_root import *
from .requests import *

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class CompanyView(APIView):
    @swagger_auto_schema(request_body=CreateCompanyRequest, responses={status.HTTP_200_OK: CompanySerializer})
    def post(self, request, *args, **kwargs):
        try:
            request_serializer = CreateCompanyRequest(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            create_company_request = request_serializer.validated_data
            company = create_company.handle(create_company_request)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(status=400, data={'error': 'Missing parameter: ' + e.args[0]})

    @swagger_auto_schema(responses={status.HTTP_200_OK: CompanySerializer(many=True)})
    def get(self, request, *args, **kwargs):
        try:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response(status=404, data={'error': 'Company not found'})

    @swagger_auto_schema(request_body=UpdateCompanyRequest, responses={status.HTTP_200_OK: CompanySerializer})
    def put(self, request, *args, **kwargs):
        try:
            request_serializer = UpdateCompanyRequest(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            update_company_request = request_serializer.validated_data
            company = update_company.handle(update_company_request)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(status=400, data={'error': 'Missing parameter: ' + e.args[0]})
        except Company.DoesNotExist:
            return Response(status=404, data={'error': 'Company not found'})


class CompanyWithQueryParamView(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: CompanySerializer})
    def get(self, request, id, *args, **kwargs):
        try:
            read_company_request = ReadCompanyRequest(id=id)
            company = read_company.handle(read_company_request)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response(status=404, data={'error': 'Company not found'})

    @swagger_auto_schema(responses={status.HTTP_200_OK: CompanySerializer})
    def delete(self, request, id, *args, **kwargs):
        try:
            delete_company_request = DeleteCompanyRequest(id)
            delete_company.handle(delete_company_request)
            return Response(status=204)
        except Company.DoesNotExist:
            return Response(status=404, data={'error': 'Company not found'})


class EmployeeView(APIView):
    @swagger_auto_schema(request_body=CreateEmployeeRequest, responses={status.HTTP_200_OK: EmployeeSerializer})
    def post(self, request, *args, **kwargs):
        try:
            request_serializer = CreateEmployeeRequest(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            create_employee_request = request_serializer.validated_data
            employee = create_employee.handle(create_employee_request)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(status=400, data={'error': 'Missing parameter: ' + e.args[0]})
        except Company.DoesNotExist:
            return Response(status=404, data={'error': 'Company not found'})

    @swagger_auto_schema(responses={status.HTTP_200_OK: EmployeeSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=404, data={'error': 'Employee not found'})

    @swagger_auto_schema(request_body=UpdateEmployeeRequest, responses={status.HTTP_200_OK: EmployeeSerializer})
    def put(self, request, *args, **kwargs):
        try:
            request_serializer = UpdateEmployeeRequest(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            update_employee_request = request_serializer.validated_data
            employee = update_employee.handle(update_employee_request)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(status=400, data={'error': 'Missing parameter: ' + e.args[0]})
        except Employee.DoesNotExist:
            return Response(status=404, data={'error': 'Employee not found'})


class EmployeeWithQueryParamView(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: EmployeeSerializer})
    def get(self, request, id, *args, **kwargs):
        try:
            read_employee_request = ReadEmployeeRequest(id=id)
            employee = read_employee.handle(read_employee_request)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=404, data={'error': 'Employee not found'})

    @swagger_auto_schema(responses={status.HTTP_200_OK: EmployeeSerializer})
    def delete(self, request, id, *args, **kwargs):
        try:
            delete_employee_request = DeleteEmployeeRequest(id)
            delete_employee.handle(delete_employee_request)
            return Response(status=204)
        except Employee.DoesNotExist:
            return Response(status=404, data={'error': 'Employee not found'})


class EntryView(APIView):
    @swagger_auto_schema(request_body=CreateEntryRequest, responses={status.HTTP_200_OK: EntrySerializer})
    def post(self, request, *args, **kwargs):
        try:
            request_serializer = CreateEntryRequest(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            create_entry_request = request_serializer.validated_data
            entry = create_entry.handle(create_entry_request)
            serializer = EntrySerializer(entry)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(status=400, data={'error': 'Missing parameter: ' + e.args[0]})
        except Employee.DoesNotExist:
            return Response(status=404, data={'error': 'Employee not found'})

    @swagger_auto_schema(responses={status.HTTP_200_OK: EmployeeSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        try:
            entries = Entry.objects.all()
            serializer = EntrySerializer(entries, many=True)
            return Response(serializer.data)
        except Entry.DoesNotExist:
            return Response(status=404, data={'error': 'Entry not found'})

    @swagger_auto_schema(request_body=UpdateEntryRequest, responses={status.HTTP_200_OK: EntrySerializer})
    def put(self, request, *args, **kwargs):
        try:
            request_serializer = UpdateEntryRequest(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            update_entry_request = request_serializer.validated_data
            entry = update_entry.handle(update_entry_request)
            serializer = EntrySerializer(entry)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(status=400, data={'error': 'Missing parameter: ' + e.args[0]})
        except Entry.DoesNotExist:
            return Response(status=404, data={'error': 'Entry not found'})


class EntryWithQueryParamView(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: EntrySerializer})
    def get(self, request, id, *args, **kwargs):
        try:
            read_entry_request = ReadEntryRequest(id=id)
            entry = read_entry.handle(read_entry_request)
            serializer = EntrySerializer(entry)
            return Response(serializer.data)
        except Entry.DoesNotExist:
            return Response(status=404, data={'error': 'Entry not found'})

    @swagger_auto_schema(responses={status.HTTP_200_OK: EntrySerializer})
    def delete(self, request, id, *args, **kwargs):
        try:
            delete_entry_request = DeleteEntryRequest(id)
            delete_entry.handle(delete_entry_request)
            return Response(status=204)
        except Entry.DoesNotExist:
            return Response(status=404, data={'error': 'Entry not found'})


class FeedView(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: EntrySerializer(many=True)})
    def get(self, request, company_id, *args, **kwargs):
        try:
            read_feed_request = GetFeedRequest(company_id)
            feed = read_feed.handle(read_feed_request)
            serializer = EntrySerializer(feed, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response(status=404, data={'error': 'Company not found'})


class TimelineView(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: EntrySerializer(many=True)})
    def get(self, request, employee_id, *args, **kwargs):
        try:
            read_timeline_request = GetTimelineRequest(employee_id)
            timeline = read_timeline.handle(read_timeline_request)
            serializer = EntrySerializer(timeline, many=True)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=404, data={'error': 'Employee not found'})

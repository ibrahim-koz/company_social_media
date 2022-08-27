from abc import ABC

from rest_framework import serializers


class CreateCompanyRequest(serializers.Serializer):
    name = serializers.CharField()


class CreateEmployeeRequest(serializers.Serializer):
    name = serializers.CharField()
    salary = serializers.IntegerField()
    company_id = serializers.IntegerField()


class CreateEntryRequest(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    employee_id = serializers.IntegerField()


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


class UpdateCompanyRequest(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)


class UpdateEmployeeRequest(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    salary = serializers.IntegerField(required=False)
    company_id = serializers.IntegerField(required=False)


class UpdateEntryRequest(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)

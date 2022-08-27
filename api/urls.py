from django.urls import path
from .views import (
    CompaniesView,
    CompanyView,
    EmployeesView,
    EmployeeView,
    EntriesView,
    EntryView,
    FeedView,
    TimelineView
)

urlpatterns = [
    path('company', CompaniesView.as_view()),
    path('company/<int:id>', CompanyView.as_view()),
    path('employee', EmployeesView.as_view()),
    path('employee/<int:id>', EmployeeView.as_view()),
    path('entry', EntriesView.as_view()),
    path('entry/<int:id>', EntryView.as_view()),
    path('feed/<int:company_id>', FeedView.as_view()),
    path('timeline/<int:employee_id>', TimelineView.as_view()),
]

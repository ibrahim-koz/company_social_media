from django.urls import path
from . import views

urlpatterns = [
    path('company', views.company),
    path('employee', views.employee),
    path('entry', views.entry),
    path('feed', views.feed),
    path('timeline', views.timeline),
]

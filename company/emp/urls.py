from django.urls import path
from .api import EmployeeCreateApi, EmployeeAPI

urlpatterns = [
    path('api/create', EmployeeCreateApi.as_view()),
    path('', EmployeeAPI.as_view()),
]

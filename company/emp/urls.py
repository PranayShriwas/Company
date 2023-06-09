from django.urls import path
from .api import EmployeeCreateApi, EmployeeAPI, UpdateEmployeeAPI, DeleteEmployeeAPI, RetrieveEmployeeAPI

urlpatterns = [
    path('api/create', EmployeeCreateApi.as_view()),
    path('', EmployeeAPI.as_view()),
    path('api/<int:pk>', UpdateEmployeeAPI.as_view()),
    path('api/delete/<int:pk>', DeleteEmployeeAPI.as_view()),
    path('api/retrieve/<int:pk>', RetrieveEmployeeAPI.as_view())
]

from django.shortcuts import render
from django.http import QueryDict
from rest_framework.response import Response
from .Serializers import StudentSerializer
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




class StudentGetApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateApi(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentReteriveApi(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

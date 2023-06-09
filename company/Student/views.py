from django.shortcuts import render
from .Serializers import StudentSerializer
from rest_framework import generics
from .models import *
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

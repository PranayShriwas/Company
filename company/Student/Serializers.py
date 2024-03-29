from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    Student_email = serializers.EmailField()
    password = serializers.CharField()

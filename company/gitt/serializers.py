from .models import Git
from rest_framework import serializers


class GitSerializer(serializers.ModelSerializer):
    model = Git
    fields = '__all__'

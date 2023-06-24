from rest_framework import serializers
from .models import Shoes
from rest_framework import generics


class ShoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = '__all__'

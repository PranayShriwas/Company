from .models import *
from rest_framework import serializers


class BagSerializer(serializers.ModelSerializer):
    model = Bag
    fields = '__all__'

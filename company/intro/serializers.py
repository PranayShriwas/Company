from .models import Intro
from rest_framework import serializers


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = '__all__'

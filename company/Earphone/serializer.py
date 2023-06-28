from rest_framework import serializers
from .models import Earphone


class EarphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earphone
        fields = '__all__'

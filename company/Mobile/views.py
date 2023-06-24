from django.shortcuts import render
from .serializers import MobileSerializer
from .models import Mobile
from rest_framework import generics
# Create your views here.


class MobileApi(generics.ListAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileCreateApi(generics.CreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileUpdateApi(generics.UpdateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileDeleteApi(generics.DestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileReteriveApi(generics.RetrieveAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

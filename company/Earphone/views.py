from django.shortcuts import render
from .serializer import EarphoneSerializer
from .models import Earphone
from rest_framework import generics
# Create your views here.


class Earphones(generics.ListAPIView):
    queryset = Earphone.objects.all()
    serializer_class = EarphoneSerializer


class EarphoneCreate(generics.CreateAPIView):
    queryset = Earphone.objects.all()
    serializer_class = EarphoneSerializer


class EarphoneDelete(generics.DestroyAPIView):
    queryset = Earphone.objects.all()
    serializer_class = EarphoneSerializer


class EarphoneUpdate(generics.UpdateAPIView):
    queryset = Earphone.objects.all()
    serializer_class = EarphoneSerializer


class EarphoneReterive(generics.RetrieveAPIView):
    queryset = Earphone.objects.all()
    serializer_class = EarphoneSerializer

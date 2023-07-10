from django.shortcuts import render
from .models import *
from rest_framework import generics
from .Serializers import BagSerializer
from rest_framework import serializers

# Create your views here.


class BagCreateApi(generics.CreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagApi(generics.ListAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagDeleteApi(generics.DestroyAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagUpdateApi(generics.UpdateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagReteriveApi(generics.RetrieveAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

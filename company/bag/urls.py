from django.urls import path
from .views import BagApi, BagCreateApi, BagDeleteApi, BagReteriveApi, BagUpdateApi
from rest_framework import generics
from .Serializers import BagSerializer
path('', BagApi.as_view()),
path('api/create', BagCreateApi.as_view()),
path('api/<int:pk>', BagUpdateApi.as_view()),
path('api/delete/<int:pk>', BagDeleteApi.as_view()),
path('api/reterive/<int:pk>', BagReteriveApi.as_view())

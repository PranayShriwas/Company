from django.urls import path
from .api import BagApi, BagCreateApi, BagDeleteApi, BagReteriveApi, BagUpdateApi
from .models import Bag
urlpatterns = [
    path('', BagApi.as_view()),
    path('api/create/', BagCreateApi.as_view()),
    path('api/delete/<int:pk>', BagDeleteApi.as_view()),
    path('api/<int:pk>', BagUpdateApi.as_view()),
    path('api/get/<int:pk>', BagReteriveApi.as_view())
]

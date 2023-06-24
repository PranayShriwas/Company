from django.urls import path
from .api import ShoesApi, ShoesCreateApi, ShoesDeleteApi, ShoesReteriveApi, ShoesUpdateApi
from .models import Shoes
urlpatterns = [
    path('', ShoesApi.as_view()),
    path('api/create', ShoesCreateApi.as_view()),
    path('api/<int:pk>', ShoesUpdateApi.as_view()),
    path('api/delete/<int:pk>', ShoesDeleteApi.as_view()),
    path('api/reterive/<int:pk>', ShoesReteriveApi.as_view())
]

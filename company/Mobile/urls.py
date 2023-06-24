from django.urls import path
from .views import MobileApi, MobileCreateApi, MobileDeleteApi, MobileReteriveApi, MobileUpdateApi
urlpatterns = [
    path('', MobileApi.as_view()),
    path('api/create', MobileCreateApi.as_view()),
    path('api/<int:pk>', MobileUpdateApi.as_view()),
    path('api/delete/<int:pk>', MobileDeleteApi.as_view()),
    path('api/reterive/<int:pk>', MobileReteriveApi.as_view())
]

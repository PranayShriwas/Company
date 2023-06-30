from django.urls import path
from .api import IntroApi, IntroCreateApi, IntroUpdateApi, IntroDeleteApi, IntroReteriveApi
urlpatterns = [
    path('', IntroApi.as_view()),
    path('api/create', IntroCreateApi.as_view()),
    path('api/<int:pk>', IntroUpdateApi.as_view()),
    path('api/delete/<int:pk>', IntroDeleteApi.as_view()),
    path('api/reterive/<int:pk>', IntroReteriveApi.as_view())
]

from django.urls import path
from .api import GitApi, GitCreateApi, GitDeleteApi, GitReteriveApi, GitUpdateApi

urlpatterns = [
    path('api/', GitApi.as_view()),
    path('api/create', GitCreateApi.as_view()),
    path('api/<int:pk>', GitUpdateApi.as_view()),
    path('api/delete/<int:pk>', GitDeleteApi.as_view()),
    path('api/reterive/<int:pk>', GitReteriveApi.as_view())

]

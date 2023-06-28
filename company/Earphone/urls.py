from django.urls import path
from .views import Earphones, EarphoneDelete, EarphoneReterive, EarphoneCreate, EarphoneUpdate
from .serializer import EarphoneSerializer
from .models import Earphone
urlpatterns = [
    path('', Earphones.as_view()),
    path('api/create', EarphoneCreate.as_view()),
    path('api/<int:pk>', EarphoneUpdate.as_view()),
    path('api/delete/<int:pk>', EarphoneDelete.as_view()),
    path('api/reterive/<int:pk>', EarphoneReterive.as_view())

]

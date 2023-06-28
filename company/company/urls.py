from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp.urls')),
    path('student/', include('Student.urls')),
    path('mobile/', include('Mobile.urls')),
    path('ear/', include('Earphone.urls'))
]

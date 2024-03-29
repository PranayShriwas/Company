from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp.urls')),
    path('student/', include('Student.urls')),
    path('mobile/', include('Mobile.urls')),
    path('ear/', include('Earphone.urls')),
    path('intro/', include('intro.urls')),
    path('bag/', include('bag.urls')),
    path('git/', include('gitt.urls'))
]

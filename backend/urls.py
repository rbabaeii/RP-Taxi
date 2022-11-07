from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/' , include('Account.urls')),
    path('api/' , include('api.urls')),
    path('drivers/' , include('drivers.urls')),
]

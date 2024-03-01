
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('MyPlant_App.web.urls')),
    path('plants/', include('MyPlant_App.plants.urls')),
    path('profiles/', include('MyPlant_App.profiles.urls')),
]

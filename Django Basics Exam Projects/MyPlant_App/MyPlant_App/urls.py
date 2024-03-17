
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('MyPlant_App.web.urls')),
    path('profiles/', include('MyPlant_App.profiles.urls')),
    path('plants/', include('MyPlant_App.plants.urls')),

)

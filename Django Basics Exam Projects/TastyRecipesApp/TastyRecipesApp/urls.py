from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('TastyRecipesApp.web.urls')),
    path('profiles/', include('TastyRecipesApp.profiles.urls')),
    path('recipes/', include('TastyRecipesApp.recipes.urls')),

)

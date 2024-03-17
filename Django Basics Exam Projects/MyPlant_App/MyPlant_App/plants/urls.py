from django.urls import path

from MyPlant_App.plants.views import catalog

urlpatterns = (
    path("catalog/", catalog, name="catalog"),
)

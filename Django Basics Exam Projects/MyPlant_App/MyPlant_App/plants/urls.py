from django.urls import path

from MyPlant_App.plants.views import PlantsCreateView

urlpatterns = (
    path("create/", PlantsCreateView.as_view(), name="create plant"),
)

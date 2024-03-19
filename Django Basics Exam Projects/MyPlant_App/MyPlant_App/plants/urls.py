from django.urls import path

from MyPlant_App.plants.views import PlantsCreateView, PlantsDetailView, PlantsUpdateView, PlantsDeleteView

urlpatterns = (
    path("create/", PlantsCreateView.as_view(), name="create plant"),
    path("details/<int:pk>/", PlantsDetailView.as_view(), name="plant details"),
    path("edit/<int:pk>/", PlantsUpdateView.as_view(), name="edit plant"),
    path("delete/<int:pk>/", PlantsDeleteView.as_view(), name="delete plant"),
)

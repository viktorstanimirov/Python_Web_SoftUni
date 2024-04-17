from django.urls import path

from TastyRecipesApp.profiles.views import CreateProfileView, DetailsProfileView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name="create-profile"),
    path("details/<int:pk>", DetailsProfileView.as_view(), name="details-profile"),
    path("edit//<int:pk>", ProfileEditView.as_view(), name="edit-profile"),
    path("delete//<int:pk>", ProfileDeleteView.as_view(), name="delete-profile"),
]
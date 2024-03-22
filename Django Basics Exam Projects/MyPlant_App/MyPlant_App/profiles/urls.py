from django.urls import path


from MyPlant_App.profiles.views import CreateProfileView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path("create/", CreateProfileView.as_view(), name="create profile"),
    path("details/<int:pk>", ProfileDetailsView.as_view(), name="details profile"),
    path("edit//<int:pk>", ProfileEditView.as_view(), name="edit profile"),
    path("delete//<int:pk>", ProfileDeleteView.as_view(), name="delete profile"),
)

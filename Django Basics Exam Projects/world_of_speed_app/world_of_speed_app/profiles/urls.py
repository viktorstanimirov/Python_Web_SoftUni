from django.urls import path

from world_of_speed_app.profiles.views import create_profile, profile_details, edit_profile, delete_profile

urlpatterns = (
    path("create-profile/", create_profile, name="create_profile"),
    path("profile_details/", profile_details, name="profile_details"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("delete-profile/", delete_profile, name="delete_profile"),
)


from django.urls import path

from my_music_app.profiles.views import profile_details, delete_profile

urlpatterns = (
    path("details/", profile_details, name="profile_details"),
    path("delete/", delete_profile, name="delete_profile"),
)
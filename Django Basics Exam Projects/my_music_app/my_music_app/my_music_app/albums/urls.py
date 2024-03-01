from django.urls import path

from my_music_app.albums.views import create_album, album_details, edit_album, delete_album

urlpatterns = (
    path("add/", create_album, name="create_album"),
    path("details/<int:pk>/", album_details, name="album_details"),
    path("edit/<int:pk>/", edit_album, name="edit_album"),
    path("delete/<int:pk>/", delete_album, name="delete_album")
)
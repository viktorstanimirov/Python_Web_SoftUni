from django.urls import path

from my_music_app.albums.views import create_album

urlpatterns = (
    path("add/", create_album, name="create_album"),
)
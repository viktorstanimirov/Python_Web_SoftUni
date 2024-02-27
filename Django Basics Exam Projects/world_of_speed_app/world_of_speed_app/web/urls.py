from django.urls import path

from world_of_speed_app.web.views import index
urlpatterns = (
    path("", index, name="index"),

)


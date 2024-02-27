from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("world_of_speed_app.web.urls")),
    path("cars/", include("world_of_speed_app.cars.urls")),
    path("profiles/", include("world_of_speed_app.profiles.urls")),

]

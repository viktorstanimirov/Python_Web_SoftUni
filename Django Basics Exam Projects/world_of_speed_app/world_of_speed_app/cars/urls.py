from django.urls import path, include

from world_of_speed_app.cars.views import create_car, catalogue, car_details, edit_car, delete_car

urlpatterns = (
    path("catalogue/", catalogue, name="catalogue"),
    path("create/", create_car, name='create_car'),
    path("cars/<int:pk>/", include([
        path("details/", car_details, name="car_details"),
        path("edit/", edit_car, name="edit_car"),
        path("delete/", delete_car, name="delete_car"),
    ]) ),
)

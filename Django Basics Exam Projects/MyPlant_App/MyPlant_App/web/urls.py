from django.urls import path

from MyPlant_App.web.views import index

urlpatterns = (
    path("", index, name="index"),


)


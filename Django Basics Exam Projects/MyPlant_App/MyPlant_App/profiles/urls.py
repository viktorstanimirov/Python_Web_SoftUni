from django.urls import path
from MyPlant_App.profiles import views


from MyPlant_App.profiles.views import CreateProfileView

urlpatterns = (
    path("create/", CreateProfileView.as_view(), name="create profile"),
)

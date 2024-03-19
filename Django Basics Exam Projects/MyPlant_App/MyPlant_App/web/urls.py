from django.urls import path


from MyPlant_App.web.views import index, catalogue

urlpatterns = (
    path("", index, name="index"),
    path("catalogue/", catalogue, name="catalogue")

)


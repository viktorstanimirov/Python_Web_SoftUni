from django.urls import path

from TastyRecipesApp.web.views import home_page, CatalogueView

urlpatterns = [
    path("", home_page, name="home-page"),
    path("catalogue/", CatalogueView.as_view(), name="catalogue")
]
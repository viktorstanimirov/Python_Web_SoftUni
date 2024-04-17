from django.urls import path

from TastyRecipesApp.recipes.views import create_recipe, RecipeDetailView, RecipeUpdateView, RecipeDeleteView

urlpatterns = [
    path("create/", create_recipe, name="create-recipe"),
    path("details/<int:pk>/", RecipeDetailView.as_view(), name="details-recipe"),
    path("edit/<int:pk>/", RecipeUpdateView.as_view(), name="edit-recipe"),
    path("delete/<int:pk>/", RecipeDeleteView.as_view(), name="delete-recipe")
]
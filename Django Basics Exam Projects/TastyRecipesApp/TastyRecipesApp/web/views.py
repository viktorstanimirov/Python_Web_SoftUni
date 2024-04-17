from django.shortcuts import render
from django.views import generic as view

from TastyRecipesApp.profiles.views import get_profile
from TastyRecipesApp.recipes.models import Recipe


def home_page(request):
    profile = get_profile()
    context = {
        "profile": profile
    }
    return render(request, "web/home-page.html", context)


class CatalogueView(view.ListView):
    model = Recipe
    profile = get_profile()
    recipes = Recipe.objects.all
    template_name = "web/catalogue.html"
    extra_context = {
        "profile": profile,
        "recipes": recipes
    }


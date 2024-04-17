from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as view

from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.profiles.views import get_profile
from TastyRecipesApp.recipes.forms import RecipeForm, RecipeUpdateForm, RecipeDeleteForm
from TastyRecipesApp.recipes.models import Recipe


def create_recipe(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = profile
            new_recipe.save()
            return redirect('catalogue')
    else:
        form = RecipeForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'recipes/create-recipe.html', context)


class RecipeDetailView(view.DetailView):
    model = Recipe
    template_name = "recipes/details-recipe.html"
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipe']
        context['ingredients_list'] = recipe.ingredients.split(", ")
        context['profile'] = get_profile()
        return context


class RecipeUpdateView(view.UpdateView):
    profile = get_profile()
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = "recipes/edit-recipe.html"
    extra_context = {
        "profile": profile
    }

    def get_success_url(self):
        return reverse_lazy("catalogue")


class RecipeDeleteView(view.DeleteView):
    profile = get_profile()
    model = Recipe
    template_name = "recipes/delete-recipe.html"
    success_url = reverse_lazy("catalogue")
    extra_context = {
        "profile": profile
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RecipeDeleteForm(initial=self.object.__dict__)

        return context

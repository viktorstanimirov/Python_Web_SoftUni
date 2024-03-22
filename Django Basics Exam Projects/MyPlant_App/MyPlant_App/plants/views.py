from django.urls import reverse_lazy
from django.views import generic as view

from MyPlant_App.plants.forms import PlantCreateForm, PlantUpdateForm, PlantsDeleteForm
from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.views import get_profile


class PlantsCreateView(view.CreateView):
    profile = get_profile()
    model = Plant
    form_class = PlantCreateForm
    template_name = "plants/create-plant.html"
    extra_context = {
        "profile": profile
    }

    def get_success_url(self):
        return reverse_lazy("catalogue")


class PlantsDetailView(view.DetailView):
    profile = get_profile()
    model = Plant
    template_name = "plants/plant-details.html"
    extra_context = {
        "profile": profile
    }


class PlantsUpdateView(view.UpdateView):
    profile = get_profile()
    model = Plant
    form_class = PlantUpdateForm
    template_name = "plants/edit-plant.html"
    extra_context = {
        "profile": profile
    }

    def get_success_url(self):
        return reverse_lazy("catalogue")


class PlantsDeleteView(view.DeleteView):
    profile = get_profile()
    model = Plant
    template_name = "plants/delete-plant.html"
    success_url = reverse_lazy("catalogue")
    extra_context = {
        "profile": profile
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PlantsDeleteForm(initial=self.object.__dict__)

        return context

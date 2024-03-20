from django.urls import reverse_lazy
from django.views import generic as view

from MyPlant_App.plants.forms import PlantCreateForm, PlantUpdateForm, PlantsDeleteForm
from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.views import get_profile


class PlantsCreateView(view.CreateView):
    profile = get_profile()
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


class PlantsDetailView(view.DetailView):
    profile = get_profile()
    model = Plant
    template_name = 'plants/plant-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


class PlantsUpdateView(view.UpdateView):
    model = Plant
    form_class = PlantUpdateForm
    template_name = 'plants/edit-plant.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class PlantsDeleteView(view.DeleteView):
    model = Plant
    template_name = 'plants/delete-plant.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PlantsDeleteForm(initial=self.object.__dict__)
        context['profile'] = get_profile()

        return context






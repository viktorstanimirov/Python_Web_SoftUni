from django.urls import reverse_lazy
from django.views import generic as view

from MyPlant_App.core.form_mixins import ReadonlyFieldsFormMixin
from MyPlant_App.plants.forms import PlantCreateForm, PlantUpdateForm
from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.views import get_profile


class PlantsCreateView(view.CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class PlantsDetailView(view.DetailView):
    profile = get_profile()
    model = Plant
    template_name = 'plants/plant-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


class PlantsUpdateView(view.UpdateView):
    profile = get_profile()
    model = Plant
    form_class = PlantUpdateForm
    template_name = 'plants/edit-plant.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class PlantsDeleteView(view.DeleteView):
    profile = get_profile()
    model = Plant
    form_class = ReadonlyFieldsFormMixin
    template_name = 'plants/delete-plant.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')





from django.urls import reverse_lazy
from django.views import generic as view

from MyPlant_App.plants.forms import PlantCreateForm
from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.views import get_profile


class PlantsCreateView(view.CreateView):
    profile = get_profile()
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'

    def get_success_url(self):
        return reverse_lazy('catalogue')



from django.shortcuts import render

from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.views import get_profile


def index(request):
    profile = get_profile()
    context = {
        "profile": profile,
    }
    return render(request, "common/index.html", context)


def catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        "profile": profile,
        "plants": plants,
    }
    return render(request, "common/catalogue.html", context)

from django.shortcuts import render

from MyPlant_App.profiles.views import get_profile


def index(request):
    profile = get_profile()
    return render(request, "common/index.html")

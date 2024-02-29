from django.shortcuts import render

from my_music_app.common.get_profile import get_profile


def index(request):
    profile = get_profile()

    if profile is None:
        return render(request, "web/home-no-profile.html")

    return render(request, "web/home-with-profile.html")


def create_profile(request):
    pass

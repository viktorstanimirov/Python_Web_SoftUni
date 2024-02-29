from django.shortcuts import render, redirect

from my_music_app.albums.models import Album
from my_music_app.common.get_profile import get_profile
from my_music_app.profiles.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form,
        "no_nav": True,
    }

    return render(request, "web/home-no-profile.html", context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "albums": Album.objects.all(),
        "no_nav": False,
        "profile": profile,

    }

    return render(request, "web/home-with-profile.html", context)


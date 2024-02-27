from django.shortcuts import render, redirect

from world_of_speed_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile,
    }

    return render(request, "web/index.html", context)




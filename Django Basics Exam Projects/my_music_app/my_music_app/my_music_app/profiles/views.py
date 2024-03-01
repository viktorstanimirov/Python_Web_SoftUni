from django.shortcuts import render, redirect

from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    total_count = Album.objects.count()

    context = {
        "profile": profile,
        "total_count": total_count,
    }
    return render(request, "profiles/profile-details.html", context)


def delete_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    if request.method == 'POST':
        albums.delete()
        profile.delete()
        return redirect('index')


    return render(request, "profiles/profile-delete.html")
